# pylint: disable=import-error
from datetime import date
from itertools import groupby
from operator import attrgetter
from typing import List
from uuid import uuid4

from src.data import StatusDTO
from src.domain.entity import Product
from src.domain.repository import ProductRepositoryInterface
from src.infra.adapter import adapt_product
from src.infra.config import DBConnectionHandler
from src.infra.entity.products_entity import ProductEntity


class ProductRepository(ProductRepositoryInterface):
    """Product repository implementation"""

    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.db_connection = db_connection

    def insert_product(self, product: Product) -> None:

        with self.db_connection as db_connection:
            try:
                adapted_product = adapt_product(product=product)
                new_product = ProductEntity(**adapted_product)

                db_connection.session.add(new_product)
                db_connection.session.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    def select_products_grouped_by_day(self) -> List[Product]:

        with self.db_connection as db_connection:
            query = db_connection.session.query(ProductEntity).order_by(ProductEntity.day).all()
            return {str(k): list(g) for k, g in groupby(query, attrgetter("day"))}

    def select_products_in_specific_day(self, day: str) -> List[Product]:

        with self.db_connection as db_connection:
            return (
                db_connection.session.query(ProductEntity).filter_by(day=day).order_by(ProductEntity.client_name).all()
            )

    def products_in_a_day(self, day: date) -> int:

        with self.db_connection as db_connection:
            return db_connection.session.query(ProductEntity).filter_by(day=day).count()

    def update_product_status(self, id: uuid4, status: StatusDTO) -> None:

        with self.db_connection as db_connection:
            try:
                db_connection.session.query(ProductEntity).filter_by(id=id).update(
                    {
                        ProductEntity.cover_status: status.cover,
                        ProductEntity.core_status: status.core,
                    }
                )

                db_connection.session.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    def delete_product(self, id: uuid4) -> None:
        with self.db_connection as db_connection:
            try:
                db_connection.session.query(ProductEntity).filter_by(id=id).delete()

                db_connection.session.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

from datetime import date
from typing import List
from uuid import uuid4

from src.data import StatusDTO
from src.domain.entity import Product
from src.domain.repository import ProductRepositoryInterface
from src.infra.adapter import adapt_product
from src.infra.config.db_base import DBConnectionHandler
from src.infra.entity.products_entity import ProductEntity


class ProductRepository(ProductRepositoryInterface):
    """Product repository implementation"""

    @classmethod
    def insert_product(cls, product: Product) -> None:

        with DBConnectionHandler() as db_connection:
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

    @classmethod
    def select_products_in_specific_day(cls, day: str) -> List[Product]:

        with DBConnectionHandler() as db_connection:
            return db_connection.session.query(ProductEntity).filter_by(day=day).all()

    @classmethod
    def is_day_limit_reached(cls, day: date) -> bool:

        with DBConnectionHandler() as db_connection:
            return (
                len(db_connection.session.query(ProductEntity).filter_by(day=day).all())
                > 10
            )

    @classmethod
    def update_product_status(cls, id: uuid4, status: StatusDTO) -> bool:

        with DBConnectionHandler() as db_connection:
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

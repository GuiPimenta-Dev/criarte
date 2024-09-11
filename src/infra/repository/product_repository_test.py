from datetime import date, datetime

from faker import Faker
from src.data import StatusDTO
from src.infra.config import DBConnectionHandler
from src.infra.repository import ProductRepository

faker = Faker()
db_connection_handler = DBConnectionHandler("sqlite:///test.db")
product_repository = ProductRepository(db_connection_handler)


def test_insert_product(product, engine):

    product_repository.insert_product(product=product)
    product_id = str(product.id)

    result = engine.execute(f"SELECT * FROM products WHERE id = '{product_id}';").fetchone()

    assert product_id == result.id
    assert product.type == result.type
    assert product.printed_name == result.printed_name
    assert product.theme == result.theme
    assert product.price == result.price
    assert product.sex == result.sex
    assert product.payment == result.payment
    assert str(product.day) == result.day
    assert product.client.name == result.client_name
    assert product.client.address == result.client_address
    assert product.client.state == result.client_state
    assert product.status.cover == result.cover_status
    assert product.status.core == result.core_status


def test_select_products_grouped_by_day(products):

    expected_result = []
    for _ in range(5):
        product = products()

        product.day = datetime.strptime(faker.date(), "%Y-%m-%d").date()
        expected_result.append(str(product.day))
        product_repository.insert_product(product=product)

    results = product_repository.select_products_grouped_by_day()
    for result in results:
        assert result in expected_result


def test_select_products_in_specific_day_must_be_5(products):

    for _ in range(5):
        product = products()
        product_repository.insert_product(product=product)

    results = product_repository.select_products_in_specific_day(day=date.today())

    assert len(results) == 5


def test_products_in_a_day(products):

    for _ in range(10):
        product = products()
        product_repository.insert_product(product=product)

    result = product_repository.products_in_a_day(day=date.today())

    assert result == 10


def test_update_product_status(product, engine):

    product_repository.insert_product(product=product)

    product_status = [(True, False), (False, True), (True, True), (False, False)]

    for status in product_status:
        cover_status, core_status = status
        product_repository.update_product_status(
            id=str(product.id), status=StatusDTO(cover=cover_status, core=core_status)
        )
        result = engine.execute(f"SELECT * FROM products WHERE id = '{str(product.id)}';").fetchone()

        assert result.cover_status == cover_status
        assert result.core_status == core_status


def test_delete_product_status(product, engine):

    product_repository.insert_product(product=product)
    result = engine.execute(f"SELECT * FROM products WHERE id = '{str(product.id)}';").fetchone()

    assert result

    product_repository.delete_product(str(product.id))

    result = engine.execute(f"SELECT * FROM products WHERE id = '{str(product.id)}';").fetchone()

    assert not result

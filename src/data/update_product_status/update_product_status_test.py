from uuid import uuid4

from src.data import StatusDTO
from src.data.update_product_status.update_product_status import UpdateProductStatus
from src.infra.test.product_spy import ProductRepositorySpy


def test_update_product_status_correctly(product):
    product_repository = ProductRepositorySpy()
    product_repository.insert_product(product)
    update_product_usecase = UpdateProductStatus(repository=product_repository)

    product_status = [(True, False), (False, True), (True, True), (False, False)]

    for status in product_status:
        cover_status, core_status = status
        update_product_usecase.update_status(id=product.id, status=StatusDTO(cover=cover_status, core=core_status))
        status = product_repository.product_by_id_params[product.id].status

        assert status.cover is cover_status
        assert status.core is core_status


def test_update_product_status_without_id_in_database():
    product_repository = ProductRepositorySpy()
    update_product_usecase = UpdateProductStatus(repository=product_repository)

    update_product_usecase.update_status(id=uuid4(), status=StatusDTO(cover=True, core=False))

    assert product_repository.product_by_id_params == {}

from src.data.delete_product import DeleteProduct
from src.infra.test.product_spy import ProductRepositorySpy


def test_delete_product(product):
    product_repository = ProductRepositorySpy()
    product_repository.insert_product(product)
    delete_product_usecase = DeleteProduct(repository=product_repository)

    assert product_repository.product_by_id_params[product.id]

    delete_product_usecase.delete_product(product.id)

    assert product.id not in product_repository.product_by_id_params

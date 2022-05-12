from typing import Dict, List

from src.controllers.presenters import present_product
from src.infra.entity.products_entity import ProductEntity


def present_products_by_day(
    products: Dict[str, List[ProductEntity]],
) -> Dict:
    results = {}
    for product_key, product_value in products.items():
        presented_products = [present_product(value) for value in product_value]
        results[product_key] = {
            "products": presented_products,
            "quantity": len(presented_products),
        }

    return results

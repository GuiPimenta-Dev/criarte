from typing import Dict

from src.domain.entity import Product


def adapt_product(product: Product) -> Dict:

    return {
        "id": str(product.id),
        "day": product.day,
        "type": product.type,
        "printed_name": product.printed_name,
        "theme": product.theme,
        "price": product.price,
        "sex": product.sex,
        "payment": product.payment,
        "observations": product.observations,
        "client_name": product.client.name,
        "client_address": product.client.address,
        "client_state": product.client.state,
        "cover_status": product.status.cover,
        "core_status": product.status.core,
    }

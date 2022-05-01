from datetime import date


class ProductRepositorySpy:
    """Spy to Product Repository"""

    def __init__(self):
        self.insert_product_params = {}

    def insert_product(
        self,
        id: str,
        name: str,
        client: str,
        completed: bool,
        observations: str,
        day: date,
    ) -> None:
        product = {
            "id": id,
            "name": name,
            "client": client,
            "completed": completed,
            "observations": observations,
            "day": day,
        }
        if day not in self.insert_product_params:
            self.insert_product_params[day] = [product]
        else:
            self.insert_product_params[day].append(product)

    def is_day_limit_reached(self, day: date) -> bool:
        if day in self.insert_product_params:
            return len(self.insert_product_params[day]) >= 10
        return False

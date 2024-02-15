from dao.order_processor_repository import OrderProcessorRepository
from entity.product import Product
from entity.customer import Customer
from typing import List, Dict
import myexceptions


class OrderProcessorRepositoryImpl(OrderProcessorRepository):
    def create_product(self, product: Product) -> bool:
        # Your implementation here
        pass

    def create_customer(self, customer: Customer) -> bool:
        # Your implementation here
        pass

    def delete_product(self, product_id: int) -> bool:
        # Your implementation here
        pass

    def delete_customer(self, customer_id: int) -> bool:
        # Your implementation here
        pass

    def add_to_cart(self, customer: Customer, product: Product, quantity: int) -> bool:
        # Your implementation here
        pass

    def remove_from_cart(self, customer: Customer, product: Product) -> bool:
        # Your implementation here
        pass

    def get_all_from_cart(self, customer: Customer) -> List[Product]:
        # Your implementation here
        pass

    def place_order(self, customer: Customer, product_quantity_map: Dict[Product, int], shipping_address: str) -> bool:
        # Your implementation here
        pass

    def get_orders_by_customer(self, customer_id: int) -> List[Dict[Product, int]]:
        # Your implementation here
        pass

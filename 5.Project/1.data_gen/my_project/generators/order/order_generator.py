from datetime import datetime

from generators.common.id_generator import IdGenerator
from generators.order.user_get import UserGet
from generators.order.store_get import StoreGet

class OrderGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        
    def generate_order(self, count):
        orders = []
        today = datetime.now()
        for _ in range(count):
            id = self.id_gen.generate_id()
            order_at = datetime.now().replace(microsecond=0)
            store_id = StoreGet.get_store()
            user_id = UserGet.get_user()
            orders.append((id, order_at, store_id, user_id))
        return orders

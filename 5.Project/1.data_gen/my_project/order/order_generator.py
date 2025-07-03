from datetime import datetime

from common.id_generator import IdGenerator
from order.user_get import UserGet
from order.store_get import StoreGet

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

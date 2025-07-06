from generators.common.id_generator import IdGenerator
from generators.orderitem.order_get import OrderGet
from generators.orderitem.item_get import ItemGet

class OrderItemGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        
    def generate_orderitem(self, count):
        order_items = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            order_id = OrderGet.get_order()
            item_id = ItemGet.get_item()
            order_items.append((id, order_id, item_id))
        return order_items

import random
import uuid

# order item id
class IdGenerator:
    def generate_id(self):
        order_item_id = uuid.uuid4()
        return order_item_id
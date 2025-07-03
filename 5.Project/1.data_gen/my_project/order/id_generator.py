import random
import uuid

# order id
class IdGenerator:
    def generate_id(self):
        order_id = uuid.uuid4()
        return order_id
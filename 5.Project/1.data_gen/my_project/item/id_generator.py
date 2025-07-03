import random
import uuid

# item id
class IdGenerator:
    def generate_id(self):
        store_id = uuid.uuid4()
        return store_id
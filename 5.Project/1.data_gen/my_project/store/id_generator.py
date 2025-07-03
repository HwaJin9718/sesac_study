import random
import uuid

# store id
class IdGenerator:
    def generate_id(self):
        store_id = uuid.uuid4()
        return store_id
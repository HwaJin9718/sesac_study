import random
import uuid

# id
class IdGenerator:
    def generate_id(self):
        id = uuid.uuid4()
        return id

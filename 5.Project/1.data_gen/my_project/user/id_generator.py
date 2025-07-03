import random
import uuid

# id
class IdGenerator:
    def generate_id(self):
        user_id = uuid.uuid4()
        return user_id
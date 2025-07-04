import random

# item price
class PriceGenerator:
    def __init__(self, file_path):
        self.price = self.load_data_from_file(file_path) # 가격

    def load_data_from_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read().splitlines()
        return data
    
    def generate_price(self):
        price = random.choice(self.price)
        return price

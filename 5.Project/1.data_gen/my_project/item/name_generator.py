import random

# item name & type
class NameGenerator:
    def __init__(self, file_path1, file_path2):
        self.itemname = self.load_data_from_file(file_path1) # 상품
        self.itemtype = self.load_data_from_file(file_path2) # 품목

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
        return data

    def generate_itemname(self):
        itemname = random.choice(self.itemname)
        return itemname
    
    def generate_itemtype(self):
        itemtype = random.choice(self.itemtype)
        return itemtype
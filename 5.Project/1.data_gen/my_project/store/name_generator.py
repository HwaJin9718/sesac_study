import random

# store name
class NameGenerator:
    def __init__(self, file_path1, file_path2):
        self.cafename = self.load_data_from_file(file_path1) # 점포이름
        self.loc = self.load_data_from_file(file_path2) # 지역

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
        return data

    def generate_loc(self):
        loc = random.choice(self.loc)
        num = random.randint(1, 10)
        return f"{loc} {num}호점"
    
    def generate_cafename(self):
        cafename = random.choice(self.cafename)
        return cafename
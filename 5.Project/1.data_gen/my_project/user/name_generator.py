import random

# name
class NameGenerator:
    def __init__(self, file_path1, file_path2):
        self.names = self.load_data_from_file(file_path1) # 이름
        self.surnames = self.load_data_from_file(file_path2) # 성

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
        return data

    def generate_name(self):
        name = random.choice(self.names)
        surname = random.choice(self.surnames)
        return f"{surname}{name}"
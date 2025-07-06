from datetime import datetime

from generators.common.id_generator import IdGenerator
from generators.user.name_generator import NameGenerator
from generators.user.birthdate_generator import BirthdateGenerator
from generators.user.gender_generator import GenderGenerator
from generators.user.address_generator import AddressGenerator

class UserGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator('data/names.txt', 'data/surnames.txt')
        self.bday_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator('data/cities.txt')
        
    def generate_user(self, count):
        users = []
        today = datetime.now()
        for _ in range(count):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            bday = self.bday_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()
            age = (today - datetime.strptime(bday, "%Y-%m-%d")).days // 365
            users.append((id, name, gender, age, bday, address))
        return users

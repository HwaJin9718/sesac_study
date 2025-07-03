from datetime import datetime

from common.id_generator import IdGenerator
from user.name_generator import NameGenerator
from user.birthdate_generator import BirthdateGenerator
from user.gender_generator import GenderGenerator
from user.address_generator import AddressGenerator

class UserGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator('names.txt', 'surnames.txt')
        self.bday_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator('cities.txt')
        
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


# Id,Name,Gender,Age,Birthdate,Address
# 0a497257-2b1a-4836-940f-7b95db952e61,강준영,Male,28,1994-09-08,대구 강서구 59길 66
# 3e00736a-5978-48ee-9aa9-366b0c4ed0b8,장승현,Female,43,1979-11-05,서울 강남구 88길 78
# 7b5dda41-7547-4660-ab66-3ad52f739fff,조하은,Male,12,2010-11-07,부산 중구 59로 2
# 0a234508-1a52-4339-9e49-9c3dcf3d8d33,장은지,Female,37,1985-12-25,광주 서구 31길 41
# 3166575b-82ca-4327-8992-767848e2afa9,최은지,Female,51,1971-10-08,서울 남구 21길 78
# e09c5eea-b984-473f-98be-7fa81361e86e,이서준,Female,35,1987-08-10,서울 중구 52길 26
# 38957748-049e-44b6-8c3e-5acfadfdedf2,조예진,Female,15,2007-12-15,서울 남구 34로 97
# 5d11492a-3d41-4241-ab3b-312c68372937,이예지,Female,29,1993-08-14,서울 서구 49로 7
# c1da6b3f-51ad-4fc4-8143-5d2b161f44ee,최서준,Female,42,1981-01-25,대구 강남구 25길 95

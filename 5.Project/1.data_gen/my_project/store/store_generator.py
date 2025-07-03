from common.id_generator import IdGenerator
from store.name_generator import NameGenerator
from store.address_generator import AddressGenerator

class StoreGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator('store.txt', 'cities.txt')
        self.address_gen = AddressGenerator('cities.txt')
        
    def generate_store(self, count):
        stores = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            cafename = self.name_gen.generate_cafename()
            name = f"{cafename} {self.name_gen.generate_loc()}"
            address = self.address_gen.generate_address()
            stores.append((id, name, cafename, address))
        return stores

# Id,Name,Type,Address
# 69568455-8856-4a61-b7a0-8e2061fd06cd,스타벅스 홍대8호점,스타벅스,부산 강남구 31로 50
# a7ba6be3-356b-422c-9250-d2ba95c470da,스타벅스 송파2호점,스타벅스,인천 강서구 15길 42
# 6d90b46e-7bab-45e3-ab88-9ff1eb393aee,투썸 강서9호점,투썸,부산 강남구 25로 57
# e687ed96-5716-451d-ba80-75e5d107c2ad,커피빈 신촌5호점,커피빈,부산 강서구 32로 45
# 72a8418b-0f81-4ee7-b57e-b8d9ff7eab73,이디야 잠실9호점,이디야,부산 강남구 74길 79
# 7951a2e8-5384-4132-8d70-0d027f976597,스타벅스 송파9호점,스타벅스,부산 강남구 43로 71
# 3a7566d7-ff3b-4698-b850-727c1374a7ea,커피빈 잠실2호점,커피빈,광주 강남구 74길 74
# 26be172c-ae2e-48a6-8613-951761be4494,이디야 잠실4호점,이디야,부산 강남구 100로 56
# 0acc9d84-726b-4e53-a27f-883759456f79,커피빈 홍대3호점,커피빈,광주 중구 91길 95
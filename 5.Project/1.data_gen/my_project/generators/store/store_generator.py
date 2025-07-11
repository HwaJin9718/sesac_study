from generators.common.id_generator import IdGenerator
from generators.store.name_generator import NameGenerator
from generators.store.address_generator import AddressGenerator

class StoreGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator('data/store.txt', 'data/cities.txt')
        self.address_gen = AddressGenerator('data/cities.txt')
        
    def generate_store(self, count):
        stores = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            cafename = self.name_gen.generate_cafename()
            name = f"{cafename} {self.name_gen.generate_loc()}"
            address = self.address_gen.generate_address()
            stores.append((id, name, cafename, address))
        return stores

from generators.common.id_generator import IdGenerator
from generators.item.name_generator import NameGenerator
from generators.item.price_generator import PriceGenerator

class ItemGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator('data/itemname.txt', 'data/itemtype.txt')
        self.price_gen = PriceGenerator('data/price.txt')
        
    def generate_item(self, count):
        items = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            itemtype = self.name_gen.generate_itemtype()
            itemname = f"{self.name_gen.generate_itemname()} {itemtype}"
            price = self.price_gen.generate_price()
            items.append((id, itemname, itemtype, price))
        return items

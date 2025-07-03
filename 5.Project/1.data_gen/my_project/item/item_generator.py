from item.id_generator import IdGenerator
from item.name_generator import NameGenerator
from item.price_generator import PriceGenerator

class ItemGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator('itemname.txt', 'itemtype.txt')
        self.price_gen = PriceGenerator('price.txt')
        
    def generate_item(self, count):
        items = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            itemtype = self.name_gen.generate_itemtype()
            itemname = f"{self.name_gen.generate_itemname()} {itemtype}"
            price = self.price_gen.generate_price()
            items.append((id, itemname, itemtype, price))
        return items


# Id,                                  Name,           Type,  UnitPrice
# aeaa187d-f30d-42db-8c23-7632f85bacef,Americano Coffee,Coffee,3000
# f543b3a2-9409-4ba5-be23-75834a916962,Strawberry Cake,Cake,5500
# d245b380-6572-4404-b809-55eea2daf7d0,Watermelon Juice,Juice,4000
# 022f1eec-5257-41dc-9985-0e289ff21046,Americano Coffee,Coffee,3000
# f1b56583-8a27-4a07-89d1-ded18794bbb6,Strawberry Cake,Cake,5500
# 8fa762e7-4898-43dd-a72c-253a043cc84c,Americano Coffee,Coffee,3000
# a7f9b9d0-cb48-43f0-9186-b6d77211a7c0,Espresso Coffee,Coffee,2500
# e530a804-38d6-4981-9bfe-60f3b4d26da9,Vanilla Cake,Cake,5000
# b285ccfc-8d3e-48aa-a69f-34ecae62ccb4,Red Velvet Cake,Cake,6500
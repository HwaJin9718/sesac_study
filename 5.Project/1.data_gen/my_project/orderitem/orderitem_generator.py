from common.id_generator import IdGenerator
from orderitem.order_get import OrderGet
from orderitem.item_get import ItemGet

class OrderItemGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        
    def generate_orderitem(self, count):
        order_items = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            order_id = OrderGet.get_order()
            item_id = ItemGet.get_item()
            order_items.append((id, order_id, item_id))
        return order_items

# Id,OrderId,ItemId
# f0b0bf5d-31fb-4a21-b55d-f96b91ea91ee,5ee7925a-80d1-4732-9dd2-04f02a805b40,f1b56583-8a27-4a07-89d1-ded18794bbb6
# 75e4d658-912b-44e9-9c75-c889736e122c,e45290bc-1c38-441b-a0eb-a1c9fdd50a09,0d8d91a1-5679-4b2f-8073-f1163285b39b
# 0b5fff26-bf92-4b08-a382-ef169c8a9915,daf860ab-5385-428c-9ba6-fe5e6b426b08,f543b3a2-9409-4ba5-be23-75834a916962
# 8009ab9a-9006-40bf-a092-9b047983909a,2092c866-fb61-44ea-a12d-336877608714,f1b56583-8a27-4a07-89d1-ded18794bbb6
# cae5fe0c-dab2-4993-8d56-18bd1211d36b,11a418d8-a44c-4088-ab40-a9c5fcb56421,aeaa187d-f30d-42db-8c23-7632f85bacef
# c6312693-8f05-43ff-afd0-99b0d3d0170a,6f48b574-790d-4055-b762-75663eed5f67,e530a804-38d6-4981-9bfe-60f3b4d26da9
# 5110c5d8-73d5-4de3-b099-9eb879fc3958,b2b2b54e-9944-4927-9b2f-f3acda8b91cd,ce647b7c-8915-4ea1-8d83-6ef54bb9c6fc
# 6412570d-2ba8-40f9-bbbb-859fcb304048,096ae872-5e62-4a00-9300-ab3029e2eafd,1d86b6a6-96a8-418c-8e6f-dc8a8b9080f0
# 492cf510-9213-4bc2-a418-d14ac1560dd4,db5bd6d6-63ef-4b96-a1cf-ce033a7aad89,d245b380-6572-4404-b809-55eea2daf7d0
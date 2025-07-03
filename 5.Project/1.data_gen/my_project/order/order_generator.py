from datetime import datetime

from common.id_generator import IdGenerator
from order.user_get import UserGet
from order.store_get import StoreGet

class OrderGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        
    def generate_order(self, count):
        orders = []
        today = datetime.now()
        for _ in range(count):
            id = self.id_gen.generate_id()
            order_at = datetime.now().replace(microsecond=0)
            store_id = StoreGet.get_store()
            user_id = UserGet.get_user()
            orders.append((id, order_at, store_id, user_id))
        return orders

# Id,OrderAt,StoreId,UserId
# ab2e716f-7614-455d-964d-f56a48eb8ba7,2023-03-26 13:37:31,528163d5-06ea-4798-b971-a2b7ebf6881c,27b5654f-1223-4ca5-8c14-d57b122824ae
# ea521e0c-d91a-4e84-b6b8-d8b6fc222bfb,2023-05-14 12:38:35,f0e4600f-c28d-4224-8c49-14efeec9be6a,a4ab9e48-13bf-4421-94d7-880da445a50d
# 763853ca-bb27-411a-bd17-77aed6f9af5a,2023-09-09 20:37:55,143ee9b6-e2b6-4759-a1fd-fcadfd2315ab,f6d589f9-9e7d-4c0b-a0b9-47385ae2a240
# cb650c36-6634-4063-93e4-625fdec9b775,2023-01-11 01:12:07,e80baa62-8196-4881-aa7e-9fcdae2476fd,7152df8d-a244-498d-a8b5-1a58b28c6e2d
# 8b491d9f-fbe2-4966-8621-d9305cd11774,2023-05-08 19:39:23,1c794b56-9ada-421b-92d6-a675e87c5e14,9fdf25de-1696-4e9d-88dc-a5b57815e317
# 0b55630d-5a2e-4586-946f-99b5749742bd,2023-02-21 03:14:58,28a9a712-95a8-48a7-9699-27d92698ebc6,ba972b03-abfc-4ce8-863c-c68ce23061f9
# d9d1575c-1b1d-45be-b4c3-892566e16b0d,2023-10-09 20:10:29,7951a2e8-5384-4132-8d70-0d027f976597,1c91f8ec-4c68-40eb-afc6-a4bd6f248709
# f72b58fc-03c7-4a2d-84d5-5e2b8d91c005,2023-06-29 19:20:14,cf8233e8-3577-4f5f-a7c1-ef40730b5fdc,d1a376d8-492b-46f5-bbf8-f5e88ac85443
# 5a588467-f6c8-43d8-9091-6c0e545867f2,2023-03-20 05:31:18,b2929807-7602-47ef-b668-921062225a6c,dd7ef5aa-ff80-4823-b63a-c5e9d4bf9213
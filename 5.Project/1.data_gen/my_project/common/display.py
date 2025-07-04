import csv

from user.user_generator import UserGenerator
from store.store_generator import StoreGenerator
from item.item_generator import ItemGenerator
from order.order_generator import OrderGenerator
from orderitem.orderitem_generator import OrderItemGenerator

class UserDisplayData(UserGenerator):
    def print_console(self, count):
        data = self.generate_user(count)
        for id, name, birthdate, age, gender, address in data:
            print(f"ID: {id}\nName: {name}\nBirthdate: {birthdate}\nAge: {age}\nGender: {gender}\nAddress: {address}\n")

    def print_csv(self, count, file_path, top_data):
        data = self.generate_user(count)

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(top_data)
            csv_writer.writerows(data)
        print(f"CSV 파일 저장 완료")

class StoreDisplayData(StoreGenerator): 
    def print_console(self, count):
        data = self.generate_store(count)
        for id, name, cafename, address in data:
            print(f"ID: {id}\nName: {name}\nCafeName: {cafename}\nAddress: {address}\n")

    def print_csv(self, count, file_path, top_data):
        data = self.generate_store(count)

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(top_data)
            csv_writer.writerows(data)
        print(f"CSV 파일 저장 완료")

class ItemDisplayData(ItemGenerator): 
    def print_console(self, count):
        data = self.generate_item(count)
        for id, itemname, itemtype, price in data:
            print(f"ID: {id}\nItemName: {itemname}\nItemType: {itemtype}\nPrice: {price}\n")

    def print_csv(self, count, file_path, top_data):
        data = self.generate_item(count)

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(top_data)
            csv_writer.writerows(data)
        print(f"CSV 파일 저장 완료")

class OrderDisplayData(OrderGenerator):
    def print_console(self, count):
        data = self.generate_order(count)
        for id, order_at, store_id, user_id in data:
            print(f"ID: {id}\nOrderAt: {order_at}\nStoreId: {store_id}\nUserId: {user_id}\n")

    def print_csv(self, count, file_path, top_data):
        data = self.generate_order(count)

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(top_data)
            csv_writer.writerows(data)
        print(f"CSV 파일 저장 완료")

class OrderItemDisplayData(OrderItemGenerator):
    def print_console(self, count):
        data = self.generate_orderitem(count)
        for id, order_id, item_id in data:
            print(f"ID: {id}\nOrderId: {order_id}\nItemId: {item_id}\n")

    def print_csv(self, count, file_path, top_data):
        data = self.generate_orderitem(count)

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(top_data)
            csv_writer.writerows(data)
        print(f"CSV 파일 저장 완료")

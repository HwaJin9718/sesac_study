# > python main.py

import sys
import csv
from user.user_generator import UserGenerator
from store.store_generator import StoreGenerator
from item.item_generator import ItemGenerator
from order.order_generator import OrderGenerator

# 사용자 입력 값
data_type = input(("데이터 유형을 입력하세요 (User, Store 또는 Item): "))
num = int(input("생성할 데이터 개수를 입력하세요: "))
output_type = input(("아웃풋 형태를 입력하세요 (csv, console): "))

my_data = None
file_path = ""
top_data = []

class UserDisplayData(UserGenerator):
    def print_console(self, count):
        data = self.generate_user(count)
        for id, name, birthdate, age, gender, address in data:
            print(f"ID: {id}\nName: {name}\nBirthdate: {birthdate}\nAge: {age}\nGender: {gender}\nAddress: {address}\n")

    def print_csv(self, count):
        data = self.generate_user(count)

        with open(file_path, "w", newline = "", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(top_data)
            csv_writer.writerows(data)
        print(f"CSV 파일 저장 완료")

class StoreDisplayData(StoreGenerator): 
    def print_console(self, count):
        data = self.generate_store(count)
        for id, name, cafename, address in data:
            print(f"ID: {id}\nName: {name}\nCafeName: {cafename}\nAddress: {address}\n")

    def print_csv(self, count):
        data = self.generate_store(count)

        with open(file_path, "w", newline = "", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(top_data)
            csv_writer.writerows(data)
        print(f"CSV 파일 저장 완료")

class ItemDisplayData(ItemGenerator): 
    def print_console(self, count):
        data = self.generate_item(count)
        for id, itemname, itemtype, price in data:
            print(f"ID: {id}\nItemName: {itemname}\nItemType: {itemtype}\nPrice: {price}\n")

    def print_csv(self, count):
        data = self.generate_item(count)

        with open(file_path, "w", newline = "", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(top_data)
            csv_writer.writerows(data)
        print(f"CSV 파일 저장 완료")

class OrderDisplayData(OrderGenerator):
    def print_console(self, count):
        data = self.generate_order(count)
        for id, order_at, store_id, user_id in data:
            print(f"ID: {id}\nOrderAt: {order_at}\nStoreId: {store_id}\nUserId: {user_id}\n")

    def print_csv(self, count):
        data = self.generate_order(count)

        with open(file_path, "w", newline = "", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(top_data)
            csv_writer.writerows(data)
        print(f"CSV 파일 저장 완료")

# 데이터 유형 확인
if data_type.lower() == "user":
    my_data = UserDisplayData()
    file_path = "users.csv"
    top_data = ["ID", "Name", "Gender", "Age", "Birthdate", "Address"]
elif data_type.lower() == "store":
    my_data = StoreDisplayData()
    file_path = "stores.csv"
    top_data = ["ID", "Name", "Type", "Address"]
elif data_type.lower() == "item":
    my_data = ItemDisplayData()
    file_path = "items.csv"
    top_data = ["ID", "Name", "Type", "UnitPrice"]
elif data_type.lower() == "order":
    my_data = OrderDisplayData()
    file_path = "orders.csv"
    top_data = ["ID", "OrderAt", "StoreId", "UserId"]
elif data_type.lower() == "orderitem":
    pass
else:
    print("일치하는 데이터 유형이 없습니다.")

# 아웃풋 형태 확인
if output_type.lower() == "csv":
    my_data.print_csv(num)
elif output_type.lower() == "console":
    my_data.print_console(num)
else:
    print("지원되지 않는 출력 형태입니다.")


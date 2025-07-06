# > python main.py

from generators.common.display import UserDisplayData, StoreDisplayData, ItemDisplayData, OrderDisplayData, OrderItemDisplayData

# 사용자 입력 값
data_type = input(("데이터 유형을 입력하세요 (User, Store 또는 Item): "))
count = int(input("생성할 데이터 개수를 입력하세요: "))
output_type = input(("아웃풋 형태를 입력하세요 (csv, console): "))

my_data = None
file_path = ""
top_data = []

# 데이터 유형 확인
if data_type.lower() == "user":
    my_data = UserDisplayData()
    file_path = "output/users.csv"
    top_data = ["ID", "Name", "Gender", "Age", "Birthdate", "Address"]

elif data_type.lower() == "store":
    my_data = StoreDisplayData()
    file_path = "output/stores.csv"
    top_data = ["ID", "Name", "Type", "Address"]

elif data_type.lower() == "item":
    my_data = ItemDisplayData()
    file_path = "output/items.csv"
    top_data = ["ID", "Name", "Type", "UnitPrice"]

elif data_type.lower() == "order":
    my_data = OrderDisplayData()
    file_path = "output/orders.csv"
    top_data = ["ID", "OrderAt", "StoreId", "UserId"]

elif data_type.lower() == "orderitem":
    my_data = OrderItemDisplayData()
    file_path = "output/order_items.csv"
    top_data = ["ID", "OrderId", "ItemId"]

else:
    print("일치하는 데이터 유형이 없습니다.")


# 아웃풋 형태 확인
if output_type.lower() == "csv":
    my_data.print_csv(count, file_path, top_data)

elif output_type.lower() == "console":
    my_data.print_console(count)

else:
    print("지원되지 않는 출력 형태입니다.")


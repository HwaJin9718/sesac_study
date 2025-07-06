import csv
import random

file_path = "output/orders.csv"

class OrderGet:

    def get_file_data():
        data = []
        with open(file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)

        return data
    
    def get_order():
        order_ids = []
        datas = OrderGet.get_file_data()
        for data in datas:
            order_ids.append(data['ID'])
        
        order_id = random.choice(order_ids)

        return order_id

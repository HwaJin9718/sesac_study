import csv
import random

file_path = "items.csv"

class ItemGet:

    def get_file_data():
        data = []
        with open(file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)

        return data
    
    def get_item():
        item_ids = []
        datas = ItemGet.get_file_data()
        for data in datas:
            item_ids.append(data['ID'])
        
        item_id = random.choice(item_ids)

        return item_id

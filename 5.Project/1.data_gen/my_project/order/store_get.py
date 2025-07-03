import csv
import random

file_path = "stores.csv"

class StoreGet:

    def get_file_data():
        data = []
        with open(file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)

        return data
    
    def get_store():
        store_ids = []
        datas = StoreGet.get_file_data()
        for data in datas:
            store_ids.append(data['ID'])
        
        store_id = random.choice(store_ids)

        return store_id



import csv
import random

file_path = "users.csv"

class UserGet:

    def get_file_data():
        data = []
        with open(file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)

        return data
    
    def get_user():
        user_ids = []
        datas = UserGet.get_file_data()
        for data in datas:
            user_ids.append(data['ID'])
        
        user_id = random.choice(user_ids)

        return user_id



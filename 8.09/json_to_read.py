import json

file_path = "8.09/test_read.json"

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
import json

data = {
    "name": "티스토리",
    "stack": "풀스택",
    "blog": "https://tistory.com",
    "github": "https://github.com"
}

file_path = "8.09/test_write.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
import json

# 1) json.loads() — строка JSON -> Python
s = '{"name": "Dias", "age": 19}'
data = json.loads(s)
print(data)          # {'name': 'Dias', 'age': 19}
print(data["name"])  # Dias

# 2) json.dumps() — Python -> строка JSON
obj = {"city": "Almaty", "temp": 5}
print(json.dumps(obj))  # {"city": "Almaty", "temp": 5}

# 3) читать JSON из файла
with open("sample-data.json", "r", encoding="utf-8") as f:
    sample = json.load(f)

print(sample["users"][0])  # первый пользователь

# 4) записать JSON в файл
sample["users"].append({"id": 4, "name": "Amina"})
with open("sample-data.updated.json", "w", encoding="utf-8") as f:
    json.dump(sample, f, ensure_ascii=False, indent=2)

print("saved sample-data.updated.json")

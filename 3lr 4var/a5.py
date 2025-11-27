import json

class Serializer:
    def to_json(obj, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=4)
            print(f"Объект успешно сериализован в файл {filename}")

data = {
    "name": "Роман",
    "age": 45,
    "city": "Тверь"
}

Serializer.to_json(data, "person.json")


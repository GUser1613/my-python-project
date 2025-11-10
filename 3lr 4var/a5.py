import json

class Serializer:
    @staticmethod
    def to_json(obj, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=4)
            print(f"Объект успешно сериализован в файл {filename}")

data = {
    "name": "Роман",
    "age": 30,
    "city": "Москва"
}


Serializer.to_json(data, "person.json")


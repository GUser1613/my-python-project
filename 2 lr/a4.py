import json

class Serializer:
   # @staticmethod
    def to_json(obj, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=4)
        print("Объект успешно сериализован в", filename)

# можно вызвать прямо через класс, без создания экземпляра
Serializer.to_json({"name": "Иван", "age": 30}, "person.json")
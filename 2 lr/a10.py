import json

data = {
    "name": "Michael",
    "age": 56,
    "is_student": False,
    "skills": ["Python", "C++", "Data Science", "Machine Learning"]
}

json_string = json.dumps(data, indent=4, ensure_ascii=False)
print(json_string)
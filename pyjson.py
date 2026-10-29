import json

# 1. Create your data using Python dictionaries and lists
data = {
    "name": "Alice",
    "age": 30,
    "is_employee": True,
    "skills": ["Python", "Data Analysis"]
}

# 2. Open a file in write mode ('w') and save the JSON data
with open("/home/pyuser/Python/output.json", "w") as file:
    json.dump(data, file, indent=4)

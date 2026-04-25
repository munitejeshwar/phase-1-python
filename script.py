import json

data = {"name": "Teja", "skill": "DevOps"}

with open("data.json", "w") as f:
    json.dump(data, f)

print("JSON created")


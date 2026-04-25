with open("data.json") as f:
    data = f.read()

if "DevOps" in data:
    print("Found DevOps")

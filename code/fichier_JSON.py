import json

x = {
    "name": "Pierre",
    "age": 41,
    "married": True,
    "divorced": False,
    "children": ("Paul", "Jacques"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4))

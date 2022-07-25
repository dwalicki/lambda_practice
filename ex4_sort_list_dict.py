list = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": 2, "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]

# print list sorted by model
print("The list printed sorting by model: ")
print(sorted(list, key=lambda i: i["model"]))

print("\r")

# sorted by model and color
print("The list printed sorting by model and color: ")
print(sorted(list, key=lambda i: (i["model"], i["color"])))

print("\r")

# sorted by model and color in descending order
print("The list printed sorting by model and color in descending order: ")
print(sorted(list, key=lambda i: (i["model"], i["color"]), reverse=True))

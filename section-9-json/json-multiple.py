db = {
    "users": {
        "ibrahimkus": {
            "firstName": "ibrahim",
            "lastName": "kus"
        },
        "hayrikus": {
            "firstName": "hayri",
            "lastName": "kus"
        },
    },
    "products": {
        "1": {
            "title": "Macbook Air",
            "price": 70000
        },
        "2": {
            "title": "Samsung S25",
            "price": 90000
        }
    }
}

import json

with open("db.json") as file:
    data = json.load(file)

# print(data["users"]["ibrahimkus"])
# print(data["products"]["2"]["price"])

# data["products"].update({
#     "3": {
#         "title": "Samsung S26",
#         "price": 90000
#     }
# })

# data["users"].update({
#     "ibrahimkus": {
#       "firstName": "ibrahim",
#       "lastName": "kus",
#       "age": 41
#     }
# })

# with open("db.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False, indent=2)
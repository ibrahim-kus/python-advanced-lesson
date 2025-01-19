# with open("product.json") as file:
#     data = file.read()

# print(data)
# print(type(data))

# serialize => encode
# deserialize => decode
import json

# json string
# data = """
#     {
#         "id":1,
#         "title":"Macbook Pro",
#         "price": 90000,
#         "rating": "4.5",
#         "category": "Bilgisayar",
#         "colors": ["Red","Blue"]
#     }
# """
# data = json.loads(data)

with open("product.json") as file:
    data = json.load(file)

print(data)
print(type(data))
print(data["title"])
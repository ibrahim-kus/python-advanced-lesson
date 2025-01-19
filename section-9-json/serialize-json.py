import json

product ={
    "id": 1,
    "title": "Ipad Pro",
    "price": 40000,
    "rating": "5.5",
    "category": "Computer",
    "colors": ["Red","Blue"]
}

print(product)
print(product["title"])
print(type(product))

# print("######")
# result = json.dumps(product) #Serialize
# print(result)
# #print(result["title"]) # HATA
# print(type(result))
# print("######")

with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, ensure_ascii=False, indent=2)
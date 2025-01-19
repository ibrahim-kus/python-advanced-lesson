data =   {
    "2": {
      "title": "Macbook Air",
      "price": 70000
    },
    "3": {
      "title": "Samsung S24",
      "price": 70000
    }
}

import json

with open("products2-json-dict.json") as file:
    products = json.load(file)

print(products["2"])
print(products["1"])

# products.update({
#     "1": {
#       "title": "Macbook Pro",
#       "price": 80000
#     }
# })

products.update({
    "2": {
      "title": "Samsung S25",
      "price": 99900
    }
})

products.pop("1")  # delete

with open("products2-json-dict.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)
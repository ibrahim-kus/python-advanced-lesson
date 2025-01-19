import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts", data = {
    "userId": 1,
    #"id": 1, auto
    "title": "new POST",
    "body": "qnew POST BODY"
})

result = response
result2 = response.text
result3 = response.json()
result4 = response.headers

print(result)
print(result2)
print(result3)
print(result4)
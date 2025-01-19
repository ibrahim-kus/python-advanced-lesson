import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

response

print(response)
print(type(response))
print(response.status_code)
print(response.headers)
print("####")
print(response.headers["Content-Type"])
print(response.url)
print("####")
print(response.text)
print("####")
print("####")
posts = json.loads(response.text)
print("first post title = " + posts[0]["title"])

for item in posts:
    if item["userId"] == 1:
        print(item["title"])
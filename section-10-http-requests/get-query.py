import requests

#response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1&completed=true")
#secondy Way
response = requests.get("https://jsonplaceholder.typicode.com/todos", params= {
    "userId": "1",
    "completed": "true"
})

todos = response.json()

result = todos

print(result)
import time
import asyncio

async def fetch_data(delay):
    print("data fetching..")
    await asyncio.sleep(delay)
    print("data fetched..")
    return {"data": "some datas"}

async def main():
    print("start")
    task = fetch_data(2)
    print("end")
    result = await task 
    print(f"Getted Data : {result}")


asyncio.run(main())


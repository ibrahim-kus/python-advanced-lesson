# import time

# def main(msg):
#     print("start")
#     time.sleep(2)
#     print(msg)

# main("Hello")
# main("Hello")

import time
import asyncio

async def main(msg):
    print("start")
    await asyncio.sleep(2)
    print(msg)

asyncio.run(main("Hello"))

#print(main("Hello")) #coroutine object

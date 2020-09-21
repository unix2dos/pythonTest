import asyncio
import time

async def test1():
    while True:
      print("test1", flush=True)
      time.sleep(1)
      # await asyncio.sleep(1)

async def test2():
    while True:
      print("test2", flush=True)
      time.sleep(1)
      # await asyncio.sleep(1)


async def run_task():
    await asyncio.gather(test1(), test2())



if __name__ == '__main__':
    asyncio.run(run_task())



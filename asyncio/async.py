import time
import asyncio

async def func1(x):
    print(x**2)
    await asyncio.sleep(1)
    await test()
    print('fun1 is done')

async def func2(x):
    print(x**0.5)
    await asyncio.sleep(1)
    await test()
    print('fun2 is done')

async def main():
    task_1 = asyncio.create_task(func1(2))
    task_2 = asyncio.create_task(func2(4))
    
    await task_1
    await task_2


async def test():
    x = 0
    while x < 100000:
        x += 1
    print('test_ done')


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))
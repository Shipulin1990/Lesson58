import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep((1 / power))
        print(f'Силач {name} поднял {i} шар.')
    print(f'Силач {name} закончил соревнования.')

def decor_time(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        rez = await func(*args, **kwargs)
        end = time.time()
        print(f'\nФункция {func.__name__} работала {round(end-start, 4)} сек.')
        return rez
    return wrapper

@decor_time
async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())

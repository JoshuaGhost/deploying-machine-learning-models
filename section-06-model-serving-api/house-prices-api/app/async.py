import asyncio
import random


async def producer(i, q: asyncio.Queue) -> int:
    temp = i**2
    await asyncio.sleep(random.randint(1, 3))
    print(f"producer {i} produced {temp}")
    await q.put(temp)


async def consumer(input_q: asyncio.Queue, output_q: asyncio.Queue) -> float:
    while True:
        await asyncio.sleep(random.randint(1, 3))
        temp = await input_q.get()
        print(f"consumer consumed {temp}")
        input_q.task_done()
        await output_q.put(temp / 3)
        output_q.task_done()


async def main():
    input_q = asyncio.Queue()
    output_q = asyncio.Queue()
    producers = [asyncio.create_task(producer(i, input_q)) for i in range(10)]
    consumers = [asyncio.create_task(consumer(input_q, output_q)) for i in range(5)]
    await asyncio.gather(*producers)
    await input_q.join()
    await output_q.join()
    print(output_q)
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    asyncio.run(main())

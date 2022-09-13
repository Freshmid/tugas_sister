import asyncio
import time

get_time = time.time()


async def tes():
    print("First Thread")
    print(f"finished at {time.time() - get_time} second\n") 
    await asyncio.sleep(4) # Menunggu selama 4 detik
    print("Second Thread")
    print(f"finished at {time.time() - get_time} second\n")

async def get():
    await asyncio.gather(tes())

asyncio.run(get())
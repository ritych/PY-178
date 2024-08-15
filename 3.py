import asyncio
import aiohttp


async def fetch(url, session, semaphore):
    async with semaphore:
        async with session.get(url) as response:
            status = response.status
            print(f"Got response with status: {status}")
            return status


async def main():
    url = "http://google.com"
    semaphore = asyncio.Semaphore(10)  # Ограничение на 10 запросов одновременно
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session, semaphore) for _ in range(10)]  # 10 запросов
        responses = await asyncio.gather(*tasks)
        print("All requests completed.")
        return responses


if __name__ == "__main__":
    asyncio.run(main())

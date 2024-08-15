import aiohttp
import asyncio


async def fetch_status(session, url, semaphore, index):
    async with semaphore:  # Ограничиваем количество одновременно выполняемых запросов
        async with session.get(url) as response:
            status = response.status
            print(f"Запрос {index}: Статус {status}")
            return status


async def fetch_all_statuses(url, num_requests, max_concurrent_requests):
    semaphore = asyncio.Semaphore(max_concurrent_requests)  # Семафор для ограничения количества запросов
    async with aiohttp.ClientSession() as session:
        # Создаем задачи для всех запросов
        tasks = [
            fetch_status(session, url, semaphore, i) for i in range(1, num_requests + 1)
        ]
        # Запускаем все запросы и собираем результаты
        statuses = await asyncio.gather(*tasks)

    return statuses


async def main(url, num_requests, max_concurrent_requests, output_file):
    # Получаем статусы всех запросов
    statuses = await fetch_all_statuses(url, num_requests, max_concurrent_requests)

    # Записываем статусы в файл
    with open(output_file, 'w') as file:
        for i, status in enumerate(statuses, 1):
            file.write(f"Запрос {i}: Статус {status}\n")

    print(f"Все {num_requests} выполнены и статусы сохранены в файле {output_file}")


# Параметры
url = "https://example.com/"
num_requests = 50
max_concurrent_requests = 10
output_file = "statuses.txt"

# Запускаем асинхронную программу
asyncio.run(main(url, num_requests, max_concurrent_requests, output_file))

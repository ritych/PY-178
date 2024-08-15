import asyncio
import aiofiles


async def create_file(index):
    """
    Используем asyncio для асинхронного создания и записи в файл

    :param index: Индекс для имени и содержания файла.
    :return: Имя созданного файла.
    """
    filename = f"file_{index}.txt"
    async with aiofiles.open(filename, 'w') as f:
        await f.write(f"File number: {index}")
    return filename


async def main():
    tasks = [create_file(i) for i in range(1, 11)]
    results = await asyncio.gather(*tasks)

    for filename in results:
        print(f"Created {filename}")


if __name__ == "__main__":
    asyncio.run(main())

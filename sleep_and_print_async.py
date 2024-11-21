import asyncio

async def sleep_and_print_async():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    await asyncio.gather(
        sleep_and_print_async(),
        sleep_and_print_async()
    )

if __name__ == "__main__":
    asyncio.run(main())
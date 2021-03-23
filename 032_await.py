#!/usr/bin/env python3
import asyncio


async def gorev1(param):
    print(param)
    x = 1
    while x <= 10:
        print(x, end=" ")
        x += 1


async def gorev2(param):
    print(param)
    x = 1
    while x <= 15:
        print(x, end=" ")
        x += 1


async def main():
    islem01 = asyncio.create_task(gorev1("görev 01 başladı"))
    islem02 = asyncio.create_task(gorev2("görev 02 başladı"))
    await islem01
    # islem bitince diğer isleme gececek
    if islem01.done():
        await islem02
    print("tüm görevler bitti...")


if __name__ == "__main__":
    asyncio.run(main())



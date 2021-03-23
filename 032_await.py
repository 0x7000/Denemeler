#!/usr/bin/env python3
import asyncio


async def gorev1(param):
    print(param)
    x = 1
    while x <= 10:
        print(x, end=" ")
        x += 1
    return x


async def gorev2(param):
    print(param)
    x = 1
    while x <= 15:
        print(x, end=" ")
        x += 1
    return x


async def main():
    islem01 = asyncio.create_task(gorev1("görev 01 başladı"))
    islem02 = asyncio.create_task(gorev2("görev 02 başladı"))
    await islem01
    # islem bitince diğer isleme gececek
    if islem01.done():
        await islem02
    print("tüm görevler bitti...")
    print("{} isleminin son değeri {},\
    {} islemin son değeri {}".format(islem01.get_name(), islem01.result(), islem02.get_name(), islem02.result()))


if __name__ == "__main__":
    asyncio.run(main())

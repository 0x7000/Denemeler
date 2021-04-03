#!/usr/bin/env python
import math


def main():
    ebob = math.gcd(36, 48)
    # greatest common divisor, en büyük ortak bölen
    # 36 - 48 | 2
    # 18 - 24 | 2
    # 9  - 12 | 3
    # 2 * 2 * 3 * 1 = 12
    print(ebob)


if __name__ == '__main__':
    main()

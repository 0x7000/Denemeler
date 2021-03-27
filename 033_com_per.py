#!/usr/bin/env python
import math


def main():
    cmp = math.comb(49, 6)  # 49 adet içinde 6 seçilecek loto :) kombinasyon
    print(f"Kombinasyon 49c6: {cmp:,} ")
    prm = math.perm(49, 6)  # 49 adet içinde sıralı olarak 6 seçilecek permütasyon
    print(f"Permutasyon 49p6: {prm:,} ")


if __name__ == '__main__':
    main()

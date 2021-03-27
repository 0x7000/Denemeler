#!/usr/bin/env python
import math


def main():
    cmp = math.comb(49, 6)  # 49 adet içinde 6 seçilecek loto :) kombinasyon
    print("Kombinasyon 49c6: {:,}".format(cmp))
    prm = math.perm(49, 6)  # 49 adet içinde sıralı olarak 6 seçilecek permütasyon
    print("Permutasyon 49p6: {:,}".format(prm))


if __name__ == '__main__':
    main()

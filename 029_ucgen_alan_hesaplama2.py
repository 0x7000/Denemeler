#!/usr/bin/env python

def main():
    # örnekte basit olsun diye 3 4 5 üçgeni ele alınmıştır
    aKenari = 5  # hipotenus = b^2 + c^2 = 25 yani 5in karesi
    bKenari = 3  # taban
    cKenari = 4  # dik kenar aynı zamanda yükseklik
    orta = (aKenari+bKenari+cKenari) / 2
    # kaynak https://en.wikipedia.org/wiki/Heron%27s_formula
    alan = (orta*(orta-aKenari)*(orta-bKenari)*(orta-cKenari)) ** 0.5
    print("Üçgenin alanı = {}".format(alan))
    # farkı bir yöntem (bKenari * ckenari) / 2
    # burda taban * yükseklik / 2
    alan2 = (bKenari * cKenari) / 2
    print("Üçgenin alanı = {}".format(alan2))


if __name__ == '__main__':
    main()

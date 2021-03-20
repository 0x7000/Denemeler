#!/usr/bin/env python

def main():
    # n1 ve n2 toplamı listedeki 3. sayıyı veriri 3. sayı kendisenden önceki sayı ile tekrar toplanır
    fib = []  # boş liste
    tekrar = int(input("Kaç tekrar: "))
    n1, n2 = 0, 1
    sayac = 0
    while sayac < tekrar:
        fib.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        sayac += 1
    print("Fibonacci serisi: {} ".format(fib))


if __name__ == '__main__':
    main()

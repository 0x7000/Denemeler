#!/usr/bin/env python
import dis


def main():
    print("Python sanal makinesi")
    print(selamla("öğrenci."))
    # kodun python içindeki akışı burda görünüyor
    dis.dis(selamla)


def selamla(isim):
    return "Merhaba {}".format(isim)


if __name__ == '__main__':
    main()

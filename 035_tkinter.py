#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import threading
from time import sleep


def main():
    # tkinter ile grafik kullanıcı arayüzü inşa etme denemesi.
    # bu denemede tkinter ile class yazmadan çalışacağız.
    # çoğu internet forumunda class yaapısı ile oop olarak anlatılıyor
    genislik = Pencere.winfo_screenwidth()
    # çalışılan monitorun genisliği örn. 1920
    yukseklik = Pencere.winfo_screenheight()
    # çalışılan monitorun yüksekliği örn. 1080
    # ekranı ortalamak için
    # 1920 / 3 = 640
    # 1080 / 3 = 360
    w = int(genislik / 3)
    h = int(yukseklik / 3)
    # penceremiz 720x200 boyutunda ve w ile h konumunda açılacak.
    ekran = "{}x{}+{}+{}".format(720, 200, w, h)
    Pencere.geometry(ekran)
    Pencere.mainloop()


def destroy_me():
    msg = messagebox.askyesno("Çıkış", "Çıkmak İstiyor musunuz?")
    # print(msg)  # msg true ise yes değilse no
    if msg:
        Pencere.destroy()
        # .destroy pencereyi ve bekleyen işlemleri sonlandırıcak,
        # sonlandırmadan evvel bekleyen işlemlerin kapanmasını veya bitmesini beklemekte fayda var
    else:
        pass


def label_degistir():
    # eğer bir forum elemanı üzerinde sürekli işlem yapılacaksa ayrı bir kanalda çalışmakta fayda var
    # threading ile kodu ayrı kanaldan çalıştırıp ana forumumuz kitlenmeden donmadan takip edeceğiz.
    kanal = threading.Thread(target=kana1)
    kanal.start()


def kana1():
    for i in range(0, 11):
        sleep(0.1)
        xlabel.config(text=i)


# genel tanımlar pencere boyutu başlık vs.
Pencere = Tk()
Pencere.title("Tkinter Denemeleri.")
Pencere.resizable(False, False)
# Pencere kapatılırken, destroy_me adlı fonksiyonu çağır.
Pencere.protocol('WM_DELETE_WINDOW', destroy_me)

xbuton = Button(Pencere, text="Yazdır.", command=label_degistir)
xbuton.bind_all("<KP_Enter>", lambda x: label_degistir())
xbuton.bind_all("<Return>", lambda x: label_degistir())
xbuton.place(x=10, y=90)

xlabel = Label(Pencere, text="Deneme Label.")
xlabel.place(x=10, y=10)


if __name__ == '__main__':
    main()

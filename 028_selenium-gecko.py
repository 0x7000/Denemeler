#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import urllib.parse


def main():
    aranan = input("Ara: ")
    site = "https://eksisozluk.com/?q={}".format(urllib.parse.quote(aranan))
    opt = Options()
    opt.headless = True
    driver = webdriver.Firefox(options=opt)
    driver.set_window_size(1024, 768)
    driver.get(site)
    try:
        entry = driver.find_elements_by_class_name("content")
        for i in entry:
            print(i.text)
    except Exception as e:
        print("Hata {}".format(e))
    finally:
        driver.quit()


if __name__ == '__main__':
    main()

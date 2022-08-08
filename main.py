from selenium import webdriver
import webbrowser
from os import startfile
from time import sleep
from datetime import datetime

m = [2, 3, 4]
path = "https://grandtrain.ru/tickets/2078001-2000000"  # Симф
# path = "https://grandtrain.ru/tickets/2078144-2000000"  # Керч
i = 0
desired = "Осталось мест"
while True:
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(f"{path}/2{m[i]}.08.2022/")
    sleep(2)
    text = driver.page_source
    driver.close()
    driver.quit()
    if desired in text:
        print(f"2{m[i]}")
        webbrowser.open(f"{path}/2{m[i]}.08.2022/")
        startfile("Rockstar.mp3")
        break
    i += 1
    i %= len(m)
    print(datetime.now())

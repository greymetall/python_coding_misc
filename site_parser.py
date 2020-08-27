# -*- coding: utf-8 -*-

# Рarser of course titles from the site skillbox.ru/code, in which part of the code is hidden under the cut button


from lxml import html
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument('headless') # опция для работы в безголовом режиме
driver = webdriver.Chrome(options=options) # загрузка драйврера
wait = WebDriverWait(driver, 15)  # Задаем ожидание (н-р до появления элемента)
driver.get('https://skillbox.ru/code')  # переходим на страницу
button = driver.find_element(By.XPATH, '//div[2]/section[1]/button') # поиск кнопки
driver.execute_script("window.scrollTo(0, 1500)") # прокрутка страницы вниз
button.click()
button.click() # два клика по кнопке для развёртывания списка курсов
time.sleep(3) # ожидание перед парсингом пока страница загрузится
page = driver.page_source # загрузка страницы из вебдрайвера
driver.close() # закрываем драйвер

html_tree = html.fromstring(page)

items_list = html_tree.xpath("//a[contains(@class, '--profession')]/div/h3[contains(@class, '{}')]"
                             .format('card__title h h--4'))

for item in items_list:
    print(item.text.replace('\u200c', '').strip(' '))

from bs4 import BeautifulSoup
import requests
import sys
import re
import pprint
import os
import time
from selenium import webdriver

path = os.getcwd()
f = open("contents_text.txt", 'r')
text_data = []

while True:
    line = f.readline()
    if not line: break
    text_data.append(line)


def get_replys(url,driver,imp_time=2,delay_time=0.1):
    driver.get(data_url)
    time.sleep(imp_time)

    while True:
        try :
            driver.find_element_by_css_selector(".u_cbox_btn_more").click()
            time.sleep(delay_time)
        except :
            break

    comments = open(path+"/comments.txt", 'a', encoding='utf-8')
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    contents = bs.select("span.u_cbox_contents")
    contents = [content.text for content in contents]

    for i in contents:
        comments.write(str(i) + '\n')

    comments.close()


browser = path+'\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(browser)
for data_url in text_data:
    get_replys(data_url, driver)


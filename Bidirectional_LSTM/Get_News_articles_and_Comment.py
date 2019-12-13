# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
기사제목, 기사와 댓글만 추출해서 리턴해주는 기능.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def get_replys(data_url, driver):
    imp_time = 2
    delay_time = 0.1
    driver.get(data_url)
    time.sleep(imp_time)
    unknown_comment = []
    while True:
        try:
            driver.find_element_by_css_selector(".u_cbox_btn_more").click()
            time.sleep(delay_time)
        except:
            break

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    contents = bs.select("span.u_cbox_contents")
    contents = [content.text for content in contents]

    for i in contents:
        unknown_comment.append(i)

    return unknown_comment #판별되지 않은 댓글 반환

def GetArticles(url, driver):
    articlesTitle = []
    articles = []
    image = None
    breq = requests.get(url)
    bsoup = BeautifulSoup(breq.content, 'html.parser')

    articlesTitle.append(bsoup.select('h3#articleTitle')[0].text)
    _text = bsoup.select('#articleBodyContents')[0].get_text().replace('\n','')
    btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}", " ")
    articles.append(btext)

    return articlesTitle, articles
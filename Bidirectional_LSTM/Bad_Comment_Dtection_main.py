# -*- coding: utf-8 -*-
'''
만든이 : 노태현
제목 : 악플탐지 프로그램
'''
import Get_News_articles_and_Comment
import Show_News
import Identification_Of_Malicious_Comments
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\\NohTaeHyun\\Desktop\\Bad_Comment_Dtection_Project\\chromedriver_win32\\chromedriver.exe') #C:\Users\NohTaeHyun\Desktop\Bad_comment _detection\chromedriver_win32
Unknown_Comment = []
ArticleTitle = []
Article = []
Known_Comment = []
_temp = []
while True:
    cur_url = driver.current_url
    # if driver.current_url != cur_url:
    #     cur_url = driver.current_url
    #     print(cur_url)
    #     print(cur_url[28:32])
    if cur_url[28:32] == "read":
        Unknown_Comment = Get_News_articles_and_Comment.get_replys(cur_url,driver)
        ArticleTitle, Article = Get_News_articles_and_Comment.GetArticles(cur_url,driver)
        print(ArticleTitle,'\n',Article,'\n',Unknown_Comment)
        while len(Known_Comment) != 0:
            Known_Comment = _temp
        if len(Unknown_Comment) > 0:
            for comment in Unknown_Comment:
                if len(comment) <= 94:
                    Known_Comment.append(Identification_Of_Malicious_Comments.Grade(comment))
                    # time.sleep(2)
                else:
                    Known_Comment.append("댓글 최대 글자수 초과")
        else :
            Known_Comment.append('댓글 없음')
        ArticleGui = Show_News.Show_News(ArticleTitle,Article,Known_Comment)
        time.sleep(1)
        while len(Unknown_Comment) != 0:
            Unknown_Comment = _temp
        driver.back()

# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter.messagebox

class Show_News():
    def __init__(self,articleTitle,articles,comment_list):
        self.window = Tk()
        self.window.title(str(articleTitle))
        self.window.geometry("1500x1000")
        self.window.resizable(True, True)
        self.articles = articles
        self.comment_list = comment_list
        self.variabletext = self.makeline(str(articles[0]))
        self.variablecomment = self.list2string(comment_list)

        #기사 부착
        self.frame1 = Frame(self.window,
                            relief = "solid",
                            width = 800,
                            height = 1000,
                            bd = 2)
        self.frame1.pack(side = LEFT, fill = 'both', expand =True)


        self.frame2 = Frame(self.window,
                            width = 700,
                            height = 1000,
                           relief = 'solid',
                            bd = 2)
        self.frame2.pack(side = RIGHT, fill = 'both', expand = True)

        self.articlestext = Text(self.frame1, width = 110)
        self.articlestext.pack(side = LEFT, fill = Y)
        self.articles_S = Scrollbar(self.frame1)
        self.articles_S.pack(side = RIGHT, fill = Y)
        self.articles_S.config(command = self.articlestext.yview)
        self.articlestext.config(yscrollcommand = self.articles_S.set)
        self.articlestext.insert(CURRENT, self.variabletext)

        self.commentText = Text(self.frame2, width = 75)
        self.commentText.pack(side = RIGHT, fill = Y)
        self.commentText_S = Scrollbar(self.frame2)
        self.commentText_S.pack(side = LEFT, fill = Y)
        self.commentText_S.config(command = self.commentText.yview)
        self.commentText.config(yscrollcommand = self.commentText_S.set)
        self.commentText.insert(CURRENT, self.variablecomment)
        self.window.mainloop()

    def list2string(self, list):
        text = ''
        for i in list:
            text = text + str(i) +'\n\n'
        print(text)
        return text

    def makeline(self,articles):
        for i in range(2, len(articles)+1):
            if articles[i-1:i] == '.':
                articles = articles[:i] + '\n\n'+articles[i:]
        articles = '\n\n\n' + articles[:]
        return articles
# title = "타이틀"
# articles = ["“의회 쿠데타 임박”…국회 로텐더홀서 무기한 농성 / “실세측근 농단, 대통령이 모를 수 있나” 文대통령 비판    자유한국당 황교안 대표가 11일 국회에서 열린 의원총회에서 발언하고 있다. 연합뉴스     자유한국당 황교안 대표가 11일 패스트트랙(신속처리안건) 법안 처리 저지를 위해 국회 본회의장 앞 로텐더홀에서 무기한 농성을 벌이기로 했다.   황 대표는 이날 오후 국회에서 열린 의원총회에서 “이제 저들은 선거법과 고위공직자범죄수사처(공수처)법마저 날치기 강행 처리를 하려 할 것”이라며 “좌파독재 완성을 위한 의회 쿠데타가 임박했다”며 농성 방침을 밝혔다.   지난달 28일 8일간의 청와대 앞 단식 농성을 마친 이후 13일만에 또다시 농성에나선 것이다.   전날 내년도 예산안 강행 처리에 항의해 본회의장에서 철야 농성을 한 한국당 의원들은 이날 오후 일단 해산했다.   황 대표는 “어제부터 집권당과 2중대 군소정당의 야합이 본격적으로 시작됐다. 어제 사건은 출발점”이라며 “다수의 횡포에 국회가 유린당하고 헌법과 법치가 무너졌다”고 주장했다.   이어 “이것은 국민과 야당을 향한 선전포고이자, 정권의 안위를 위해 무슨 일이든 벌이겠다고 하는, 제1야당에 대한 노골적인 협박”이라며 “몸이 부서지는 한이 있더라도 좌파독재를 반드시 막아내고 민주주의를 지켜내야 한다”고 강조했다.   황 대표는 “예산안 날치기에 가담한 사람들은 법적 책임을 비롯해 응당한 책임을 지게 하겠다”며 “국민과 함께 국민 세금 수호 투쟁으로 전개할 것”이라고 밝혔다.   그러면서 “저들의 기습적 날치기는 ‘국정농단 3대 게이트’ 등 청와대발 악재를 은폐하려는 것”이라며 “진실이 덮어지지 않는다. 오늘 출범한 진상조사본부가 한 점의혹 없이 몸통을 밝혀내고 맞서 싸울 것”이라고 덧붙였다.      자유한국당 황교안 대표, 심재철 원내대표 등 의원들이 11일 국회에서 열린 의원총회에서 손팻말을 들고 을 외치고 있다. 연합뉴스     앞서 황 대표는 이날 오전 한국당을 제외한 여당과 일부 야당이 내년도 예산안 수정안을 강행 처리한 데 대해 “우리가 소중하게 여기고 지키고자 피를 흘리고 목숨을 바쳐서 지켜왔던 대한민국의 자유민주주의가 무너졌다”고 강력 비판했다.   그러면서 집권여당 등을 겨냥, “이제 민주주의의 마지막 종언을 고하는 선거법, 공수처법을 처리하려고 할 것”이라며 “정말 목숨걸고 막겠다”고 강조했다.   황 대표는 “국민들의 뜻은 무시했고 제1 야당의 뜻은 짓밟혔다. 제멋대로 예산을 배분해"]
# comments = ["댓글1","댓글2","댓글3"]
# a = Show_News(title, articles, comments)
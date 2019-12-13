'''
뉴스 댓글을 크롤링한 데이터 중 90글자가 넘어가는 댓글을 제거처리 하는 기능.
'''
def read_data(filename):
    maxlen = 90
    result = open('refinedcomments.txt', 'a', encoding = 'utf-8')
    datas = []
    f = open(filename, 'r', encoding = 'utf-8')
    while True:
        line = f.readline()
        if not line:
            break
        else :
            datas.append(line)
    f.close()

    for data in datas:
        print(data)
        if len(data) <= maxlen :
            result.write(data+'\n')

    result.close()

read_data('comments.txt')

import os

path = os.getcwd()
os.chdir(path+'\\Movie_rating_data')
def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data

def count_Maxlen(comments):
    maxlen = 0
    for comment in comments:
        comment_len = len(comment[1])
        print(comment[1])
        if maxlen < comment_len:
            maxlen = comment_len

    return maxlen

data = read_data('ratings_train.txt')
maxlen = count_Maxlen(data)
print(maxlen)


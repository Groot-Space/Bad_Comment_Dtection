


f = open('for_ratingsdata.txt', 'r', encoding = 'utf-8')
r = open('for_ratingdata2.txt', 'a', encoding = 'utf-8')
count = 1
while True:
    s = f.readline()
    if s == None :
        break
    elif count % 2 == 1 :
        r.write(s)
    count += 1

f.close()
r.close()
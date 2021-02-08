import csv
f = open('서울지역데이터(분석용).csv', encoding='cp949')
data = csv.reader(f)
for row in data :
    print(row)
f.close()

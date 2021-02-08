# 변수 초기화
# while 조건:
#   반복할 문장
#   변수 증감식

#1부터 10까지의 합계 구하기
total = 0 #합계 구할 total 변수 0으로 초기화
i = 1
while i < 11:     #i변수가 1부터 10까지 1씩 증가
    total += i
    print("i :", i, "total :", total)
    i += 1
    
#시작값부터 종료값까지의 합계 구하기
시작값 = int(input("시작값 입력 : "))
종료값 = int(input("종료값 입력 : "))
i = 시작값
total = 0 #합계 구할 total 변수 0으로 초기화
while i < 종료값 + 1:    #i변수가 시작값부터 종료값까지 1씩 증가
    total += i
    print("i :", i, "total :", total)
    i += 1

#기온 합계 구하기
기온 = [0, 2, 5, 10, 15, 25, 28, 27, 24, 19, 12, 3]
total = 0
i = 0
while i < len(기온):
    total += 기온[i]
    print("i :", i, "total :", total)
    i += 1

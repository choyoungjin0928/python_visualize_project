# for 변수 in 조건 :
#     반복할 문장

#1부터 10까지의 합계 구하기
total = 0 #합계 구할 total 변수 0으로 초기화
for i in range(1, 10+1, 1): #i변수가 1부터 10까지 1씩 증가
    total += i
    print("i :", i, "total :", total)
    
#시작값부터 종료값까지의 합계 구하기
시작값 = int(input("시작값 입력 : "))
종료값 = int(input("종료값 입력 : "))
total = 0 #합계 구할 total 변수 0으로 초기화
for i in range(시작값, 종료값 + 1, 1): #i변수가 시작값부터 종료값까지 1씩 증가
    total += i
    print("i :", i, "total :", total)


#소수는 1과 자신의 수로만 나누어지는 수
#예) 2. 3. 5. 7. 11. 13. 17, ...
#1부터 100까지의 수 중에서 소수 구하기

count = 0 #소수여부 판단하기 위한 변수
n = int(input("1보다 큰 정수 입력 : "))
for i in range(2, n, 1):
    if n % i == 0:
        count = 1
        break
if count == 0 :
    print("소수입니다.")
else:
    print("소수가 아닙니다.")

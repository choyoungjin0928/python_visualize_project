count = 0 #소수여부 판단하기 위한 변수
n = int(input("1보다 큰 정수 입력 : "))
for i in range(2, n//2, 1):
    if n % i == 0:
        count = 1
        break
if count == 0 :
    print("소수입니다.")
else:
    print("소수가 아닙니다.")

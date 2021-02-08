import math
import time
count1 = 0
n = int(input("1보다 큰 정수 입력 : "))
start1 = time.time()
for i in range(2, n, 1):
    if n % i == 0 :
        count1 = 1
        break
end1 = time.time()
if count1 == 0 :
    print("소수입니다")
else :
    print("소수가 아닙니다")
count2 = 0
start2 = time.time()
for i in range(2, n//2, 1):
    if n % i == 0 :
        count2 = 1
        break
end2 = time.time()
if count2 == 0 :
    print("소수입니다")
else :
    print("소수가 아닙니다")
count3 = 0
start3 = time.time()
for i in range(2, int(math.sqrt(n))+1, 1):
    if n % i == 0 :
        count3 = 1
        break
end3 = time.time()
if count3 == 0 :
    print("소수입니다")
else :
    print("소수가 아닙니다")
print("초급코드 : ", end1 - start1)
print("중급코드 : ", end2 - start2)
print("고급코드 : ", end3 - start3)

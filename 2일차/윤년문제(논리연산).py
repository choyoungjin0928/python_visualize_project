n = int(input("연도 입력 : "))

if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0):
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")
    

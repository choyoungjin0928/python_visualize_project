n = int(input("연도 입력 : "))

if (n % 400 == 0) :
    print("윤년입니다.")
else:
    if (n % 4 ==0):
        if (n % 100 != 0):
            print("윤년입니다.")
        else:
            print("윤년이 아닙니다.")
    else:
        print("윤년이 아닙니다.")

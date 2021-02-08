def dictionary():
    dicA = ["love", "청출어람", "chance"]
    dicB = ["사랑", "제자나 후배가 스승이나 선배보다 나음을 말함", "기회"]
    while True:
        a = int(input("1. 단어입력, 2. 단어 검색, 3. 종료 >>> "))
        if (a == 1):
            b = input("기억할 단어 : ")
                if (b == "love"):
                    print('[',b,']',"의 의미 : ", dicB[0])
                elif (b == "청출어람"):
                    print('[',b,']',"의 의미 : ", dicB[1])
                else:
                    print('[',b,']',"의 의미 : ", dicB[2])
        elif (a == 2):
            b = input("검색할 단어 : ")
                if (b == "love"):
                    print("검색할 단어 : ", dicB[0])
                elif (b == "청출어람"):
                    print("검색할 단어 : ", dicB[1])
                else:
                    print("검색할 단어 : ", dicB[2])
        else :
            break

dictionary()

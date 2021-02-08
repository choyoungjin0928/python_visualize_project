# <리스트 복습>

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(a[0]) # indexing 인덱싱 -> 인덱스로 값을 추출, 인덱스는 반드시 0부터 시작
print(a[1])
# slicing 슬라이싱 -> 인덱스 시작과 종료를 기준으로 값을 추출.
print(a[0:2])
print(a[1:3])
print(a[:4])
print(a[2:]) # index 2번부터 끝까지 출력
print(a[-1]) # 맨 마지막 인덱스

print(a[-2:-5]) # 오른쪽값에서 왼쪽값을 뺀 갯수만큼 출력하기 때문에 음수가 나오면 안된다.
print(a[-2:])
print(len(a))
print(len(a)//2) # 인덱스 중간값 계산

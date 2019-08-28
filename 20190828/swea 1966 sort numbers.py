data_len = int(input())

for i in range(data_len):
    length = int(input())  # 입력 받을 숫자열의 길이
    num = [int(x) for x in input().split()] # 숫자열 입력
    num = sorted(num)  # 입력 받은 숫자열을 오름 차순 정렬
    num = [str(x) for x in num]  # 리스트를 이루고 있는 요소들을 문자 형채로 형 변환
    print('#%d'%(i+1), end=' ')
    print(' '.join(num))  # 리스트를 공백으로 join
test_number = int(input())
for i in range(test_number):
    word = input()

    if word == word[::-1]:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')
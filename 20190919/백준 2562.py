'''
백준 2562 최댓값
'''

numbers = []
for i in range(9):
    numbers.append(int(input()))

print(max(numbers))
print(numbers.index(max(numbers)) + 1)
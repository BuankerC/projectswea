'''
백준 2675 문자열 반복
'''

from sys import stdin

case_number = int(input())
tc = stdin.readlines()
total_test = []

for i in tc:
    test = list(i.split())
    test_num = int(test[0])
    test_sample = str(test[1])

    test_result = []

    for k in test_sample:
        print(k * test_num, end='')
    print('')
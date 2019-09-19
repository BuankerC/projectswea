'''
백준 10951 A+B - 5
'''
while(True):
    A, B = list(map(int, input().split()))
    if(A == 0 and B == 0):
        break
    else:
        print(A + B)
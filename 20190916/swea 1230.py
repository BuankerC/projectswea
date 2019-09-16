'''
swea 1230 암호문3 D3
'''

for tc in range(10):
    o, or_list = int(input()), list(input().split())
    order,lists = int(input()),  list(input().split())
    for i in range(len(lists)):
        if lists[i] == 'I':
            a =  lists[i+3:(i+2)+int(lists[i+2])+1]
            r = 0
            for j in a:
                or_list.insert(int(lists[i+1])+r,j)
                r+=1
        elif lists[i] == "D":
            index = int(lists[i+1])
            for s in range(int(lists[i+2])):
                del or_list[index]
        elif lists[i] == 'A':
            index = int(lists[i+1])
            for a in range(1,index+1):
                or_list.append(lists[i+1+a])
    print(f"#{tc+1} {' '.join(or_list[0:10])}")
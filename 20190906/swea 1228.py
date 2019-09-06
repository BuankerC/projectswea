for tc in range(1, 11):
    N = int(input())
    code = input().split()
    instruct_num = int(input())
    instructions = input().split()
    while instruct_num > 0:
        instruct = instructions.pop(0)
        instruct_num -= 1
        insert_matrix = []
        if instruct == 'I':
            start_idx = int(instructions.pop(0))
            insert_nums = int(instructions.pop(0))
            for i in range(insert_nums):
                insert_matrix += [instructions.pop(0)]
            code = code[:start_idx] + insert_matrix + code[start_idx : ]
    print('#{0}'.format(tc), end=' ')
    for i in range(10):
        print('{0}'.format(code[i]), end=' ')
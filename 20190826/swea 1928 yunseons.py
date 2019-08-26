keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
table = {value: index for index, value in enumerate(keys)}

for t in range(int(input())):
    base = list(input())
    decode = []
    binary = []
    binary24 = []
    for i in base:
        decode.append(table[i])
    for i in decode:
        a = bin(i)[2:]
        while len(a) < 6:
            a = '0' + a
        binary.append(a)
    for n in range(0, len(binary), 4):
        binary24.append(binary[n] + binary[n + 1] + binary[n + 2] + binary[n + 3])
    string = ''
    for m in binary24:
        string += chr(int(m[0:8], 2))
        string += chr(int(m[8:16], 2))
        string += chr(int(m[16:24], 2))
    print('#' + str(t + 1), string)
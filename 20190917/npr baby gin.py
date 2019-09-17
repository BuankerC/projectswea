inputs = ['124783', '667767', '054060', '101123']

def perm(n, k):
    global babygin
    if n == k:
        run = 0
        tri = 0
        if p[0] == p[1] == p[2]:
            tri += 1
        if p[3] == p[4] == p[5]:
            tri += 1
        if int(p[0])+1 == int(p[1]) and int(p[0])+2 == int(p[2]):
            run += 1
        if int(p[3])+1 == int(p[4]) and int(p[3])+2 == int(p[5]):
            run += 1
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n + 1, k)
            p[n], p[i] = p[i], p[n]

p = inputs[0]
perm(0, 6)
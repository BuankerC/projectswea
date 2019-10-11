'''
swea 4751. 다솔이의 다이아몬드 장식 D3
'''

def Alpha(word):
    A = '..#..'
    B = '.#.#.'
    C = '#.' + word + '.#'
    return ('{}\n{}\n{}\n{}\n{}'.format(A,B,C,B,A))

def Beta(word):
    t = len(word)
    A = '..#.' * t + '.'
    B = '.#.#' * t + '.'
    C = ['#']
    for a in word:
        C.append('.{}.#'.format(a))
    return ('{}\n{}\n{}\n{}\n{}'.format(A,B,''.join(C),B,A))

T = int(input())
for tc in range(T):
    word = str(input())
    if len(word) == 1:
        print(Alpha(word))
    else:
        print(Beta(word))
"""
Rotate Image

順時鐘
1 2 3   7 8 9   7 4 1
4 5 6 > 4 5 6 > 8 5 2
7 8 9   1 2 3   9 6 3
對第一維陣列反轉, 斜對稱互換

逆時鐘
1 2 3   3 2 1   3 6 9
4 5 6 > 6 5 4 > 2 5 8
7 8 9   9 8 7   1 4 7
對第二維陣列反轉, 斜對稱互換

斜對稱互換(3X3)
0,1 <> 1,0
0,2 <> 2,0
1,2 <> 2,1
i=0, j=1,2
i=1, j=2

"""


def clockwise(A):
    A.reverse()
    for i in range(0, len(A)):
        for j in range(i + 1, len(A[i])):
            A[i][j], A[j][i] = A[j][i], A[i][j]


def anticlockwise(A):
    for it in A:
        it.reverse()
    for i in range(0, len(A)):
        for j in range(i + 1, len(A[i])):
            A[i][j], A[j][i] = A[j][i], A[i][j]


def show(A):
    text = ''
    for i in range(len(A)):
        if len(text) != 0:
            text += '\n'
        for j in range(len(A[0])):
            text += f'{A[i][j]} '

    print(text)


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('===clockwise===')
    show(A)
    clockwise(A)
    print('to')
    show(A)

    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('\n===anticlockwise===')
    show(A)
    anticlockwise(A)
    print('to')
    show(A)

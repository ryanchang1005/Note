"""
Spiral Matrix
旋轉矩陣

1 2 3
4 5 6  >> [1, 2, 3, 6, 9, 8, 7, 4, 5]
7 8 9

用4個值row_start, row_end, col_start, col_end
走完上面row_start++
走完右邊col_end--
走完下面row_end--
走完左邊col_start++

"""


def run(A):
    ret = []
    row_start = 0
    row_end = len(A) - 1
    col_start = 0
    col_end = len(A[0]) - 1
    while row_start <= row_end and col_start <= col_end:
        # 跑上面
        for i in range(col_start, col_end + 1):
            ret.append(A[row_start][i])
        row_start += 1

        # 跑右邊
        for i in range(row_start, row_end + 1):
            ret.append(A[i][col_end])
        col_end -= 1

        # 跑下面
        if row_start <= row_end and col_start <= col_end:
            for i in range(col_end, col_start - 1, -1):
                ret.append(A[row_end][i])
            row_end -= 1

        # 跑左邊
        if row_start <= row_end and col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                ret.append(A[i][col_start])
            col_start += 1
    return ret


if __name__ == '__main__':
    print(run([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))

    print(run([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]))

    print(run([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]))

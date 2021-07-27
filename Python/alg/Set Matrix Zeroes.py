"""
Set Matrix Zeroes

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

         j
       i 1 1 1    1 0 1
         1 0 1 >> 0 0 0
         1 1 1    1 0 1

思路
    先檢查第一row和col有沒有0(最後再填滿0)
    再從A[1][1]開始找出0, 如果有那請把最上(A[i][0])和最左設為0(A[0][j])
    最後遍歷A[1][1] >> A[n][n], 如最上或最左有0那就設A[i][j]為0
    其實就是盡量減少重複
"""


def run(A):

    # check first col has any 0
    first_col_has_0 = False
    for i in range(len(A)):
        if A[i][0] == 0:
            first_col_has_0 = True
            break

    # check first row has any 0
    first_row_has_0 = False
    for j in range(1, len(A[0])):
        if A[0][j] == 0:
            first_row_has_0 = True
            break

    # check A[i][j] is 0
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][j] == 0:
                # set top and left 0
                A[i][0] = A[0][j] = 0

    # set 0 to A[i][j]
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][0] == 0 or A[0][j] == 0:
                A[i][j] = 0

    # set 0 to first col
    if first_col_has_0 == True:
        for i in range(len(A)):
            A[i][0] = 0

    # set 0 to first row
    if first_row_has_0 == True:
        for j in range(1, len(A[0])):
            A[0][j] = 0
    return A


if __name__ == '__main__':
    # [[1,0,1],[0,0,0],[1,0,1]]
    print(run([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))

    # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    print(run([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))

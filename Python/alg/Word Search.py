"""
Word Search
回傳在陣列中找不找的出word的路徑

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

遍歷所有陣列的元素當作起點, 往上下左右dfs, 先比較第0個字元, 往下比對第1個字元, 以此類推, 直到結束

def dfs:
    if len(word) == 0:
        OK
    if i, j越界:
        NO
    if word[0] != A[i][j]:
        NO
    下一層
    暫存當前值等等換回來(避免重複訪問)
    ret = dfs(上下左右)
    換回剛剛的值
    回傳ret
"""


def dfs(A, i, j, target_word):
    # 查完OK
    if len(target_word) == 0:
        return True

    # 越界
    if i < 0 or j < 0 or i >= len(A) or j >= len(A[i]):
        return False

    # 不等於
    if A[i][j] != target_word[0]:
        return False

    tmp = A[i][j]
    A[i][j] = "@"
    ret = dfs(A, i+1, j, target_word[1:]) or dfs(A, i-1, j, target_word[1:]) or dfs(
        A, i, j+1, target_word[1:]) or dfs(A, i, j-1, target_word[1:])
    A[i][j] = tmp
    return ret


def run(A, word):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if dfs(A, i, j, word):
                return True
    return False


if __name__ == '__main__':
    print(run(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]],
        "ABCCED"
    ))  # True

    print(run(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]],
        "SEE"
    ))  # True

    print(run(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]],
        "ABCB"
    ))  # False

    print(run(
        [["A", "B"],
         ["Z", "C"],
         ["X", "D"],
         ["F", "E"],
         ["G", "H"], ],
        "ABCDEFGH"
    ))  # True

"""
Palindromic Substrings
統計有回文的子字串陣列

Input: "abc"
Output: 3

Input: "aaa"
Output: 6

遍歷每個index, 並且左右擴展開來(i, j)(i--, j++), 須考慮兩種情況, 長度為奇數(i, i)和偶數(i, i + 1)
"""


def run(s):
    count = 0
    for i in range(len(s)):
        count += expand(s, i, i)  # 單數
        count += expand(s, i, i + 1)  # 偶數
    
    return count


def expand(s, i, j):
    count = 0
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
        count += 1
    return count


if __name__ == '__main__':
    print(run('abc'))  # 3
    print(run('aaa'))  # bb

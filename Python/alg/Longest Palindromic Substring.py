"""
Longest Palindromic Substring
找出最長回文的子字串

Input: s = 'babad'
Output: 'bab'

Input: s = 'cbbd'
Output: 'bb'

Input: s = 'a'
Output: 'a'

Input: s = 'wwssabcbakaba'
Output: 'abcba'

遍歷每個index, 並且左右擴展開來(i, j)(i--, j++), 須考慮兩種情況, 長度為奇數(i, i)和偶數(i, i + 1)

"""


def run(s):
    ret = ''
    for i in range(len(s)):
        # 單數
        tmp = expand(s, i, i)
        if len(tmp) > len(ret):
            ret = tmp

        # 偶數
        tmp = expand(s, i, i + 1)
        if len(tmp) > len(ret):
            ret = tmp
    return ret


def expand(s, i, j):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i + 1: j]  # 會因為最後一圈多加, 所以i需要加回來, j需要-1


if __name__ == '__main__':
    print(run('babad'))  # bab
    print(run('cbbd'))  # bb
    print(run('a'))  # a
    print(run('wwssabcbakaba'))  # 'abcba'

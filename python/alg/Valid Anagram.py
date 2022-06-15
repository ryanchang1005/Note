"""
Valid Anagram
驗證t是否為s的字謎(不同位置)

Input: s = "anagram", t = "nagaram"
Output: true

先用map去紀錄s個字母出現的次數++
再用t去找map去--
只要有不為0則false

"""


def run(s, t):
    m = {}

    for it in s:
        if it not in m:
            m[it] = 0
        m[it] += 1

    for it in t:
        if it not in m:
            return False
        m[it] -= 1

    for k, v in m.items():
        if v != 0:
            return False
    return True


if __name__ == '__main__':
    print(run("anagram", "nagaram"))  # True
    print(run("rat", "car"))  # False

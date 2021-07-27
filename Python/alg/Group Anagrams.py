"""
Group Anagrams
將類似的字組分群

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

直覺想到就是用map
同一種key(字串排序後相同, 出現的字元數相同)的就加再一起
"""


def run(A):
    m = {}
    for it in A:
        sorted_str = ''.join(sorted(it))  # sort str
        if sorted_str not in m:
            m[sorted_str] = []
        m[sorted_str].append(it)
    return [v for k, v in m.items()]


if __name__ == '__main__':
    # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(run(["eat", "tea", "tan", "ate", "nat", "bat"]))

    # ["abc", "acb", "bac", "cab", "bca", "cba"]
    print(run(["abc", "acb", "bac", "cab", "bca", "cba"]))

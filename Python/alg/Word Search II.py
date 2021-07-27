"""
Word Search II
與原題Word Search類似
但要找多個word

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

思路
    先把要找的words塞進Trie字典樹這個結構
    一樣遍歷整個陣列, 並與trie一起dfs下去
Trie
        t
       / \
      o   e
     /   / \
    o   e   a
['too', 'tee', 'tea']
"""
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


def dfs(A, node, i, j, word, res):
    if node.isWord:
        res.append(word)
        node.isWord = False  # 避免重複

    # 越界
    if i < 0 or j < 0 or i >= len(A) or j >= len(A[i]):
        return False

    tmp = A[i][j]
    node = node.children.get(tmp)
    if not node:
        return

    A[i][j] = "@"
    dfs(A, node, i + 1, j, word + tmp, res)
    dfs(A, node, i - 1, j, word + tmp, res)
    dfs(A, node, i, j + 1, word + tmp, res)
    dfs(A, node, i, j - 1, word + tmp, res)
    A[i][j] = tmp


def run(A, words):
    res = []
    trie = Trie()
    node = trie.root

    for word in words:
        trie.insert(word)

    for i in range(len(A)):
        for j in range(len(A[i])):
            dfs(A, node, i, j, "", res)
    return res


if __name__ == '__main__':
    print(run(
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"]
        ],
        ["oath", "pea", "eat", "rain"]
    ))  # ["eat","oath"]

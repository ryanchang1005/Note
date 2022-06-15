"""
Design Add and Search Words Data Structure

"""
import collections


class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]


if __name__ == '__main__':
    d = new WordDictionary()
    d.addWord("bad")
    d.addWord("dad")
    d.addWord("mad")
    d.search("pad")  # False
    d.search("bad")  # True
    # d.search(".ad")  # True
    # d.search("b..")  # True

"""
Binary Tree Level Order Traversal

    3
   / \
  9  20
    /  \
   15   7
[
  [3],
  [9,20],
  [15,7]
]

DFS
    建一個array, index為level, 並把array和level傳進下一層
    回傳array
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def run(root):
    ret = []

    def dfs(node, level):
        if not node:
            return
        if len(ret) < level + 1:
            ret.append([])
        ret[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    dfs(root, 0)
    return ret


if __name__ == '__main__':
    # [[3], [9, 20], [15, 7]]
    node = Node(3, Node(9), Node(20, Node(15), Node(7)))
    print(run(node))

    # [[3], [9], [1, 2]]
    node = Node(3, Node(9, Node(1), Node(2)), None)  
    print(run(node))

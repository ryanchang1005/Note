"""
Invert Binary Tree

     4
   /   \
  2     7
 / \   / \
1   3 6   9

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def show(node):
    if not node:
        return

    print(node.val)

    show(node.left)
    show(node.right)


def invert(node):
    if not node:
        return None

    tmp = node.left
    node.left = node.right
    node.right = tmp

    invert(node.left)
    invert(node.right)


if __name__ == '__main__':
    node = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
    show(node)
    print('---')
    invert(node)
    show(node)

"""
Subtree of Another Tree
判斷子樹中有沒有另一棵樹

s:
     3
    / \
   4   5
  / \
 1   2
t:
   4 
  / \
 1   2
return true

s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
t:
   4
  / \
 1   2
return false

def dfs(s,t)
    if(isSame(s,t))  # 先以兩樹一模一樣為前提
    return dfs(s.left, t) || dfs(s.right, t)  # 判斷左子樹 或 右子樹
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSame(s, t):
    if s == t == None:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False
    return isSame(s.left, t.left) and isSame(s.right, t.right)


def isSubTree(s, t):
    if s == None:
        return False
    if isSame(s, t):
        return True
    return isSubTree(s.left, t) or isSubTree(s.right, t)


if __name__ == '__main__':
    s = Node(3, Node(4, Node(1), Node(2)), Node(5))
    t = Node(4, Node(1), Node(2))
    print(isSubTree(s, t))

    s = Node(3, Node(4, Node(1), Node(2, Node(0), None)), Node(5))
    t = Node(4, Node(1), Node(2))
    print(isSubTree(s, t))

"""
Linked List Cycle
判斷一個Linked List有循環

用two pointer, 一個一次一步, 另一個兩步, 如果遇見(pointer相同, 不是值)則循環表示循環

"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def run(node):
    slow = node
    fast = node
    while slow and slow.next and fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    n3 = Node(3)
    n2 = Node(2)
    n1 = Node(1)

    n1.next = n2
    n2.next = n3
    n3.next = n1

    print(run(n1))  # True

    n3 = Node(3)
    n2 = Node(2)
    n1 = Node(1)

    n1.next = n2
    n2.next = n3

    print(run(n1))  # False

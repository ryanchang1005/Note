class Node:

    def __init__(self, val, next):
        self.val = val
        self.next = next


def reverse(node):
    head = node
    new_head = None
    while head:
        next = head.next
        head.next = new_head
        new_head = head
        head = next
    return new_head


def show(node):
    cur = node
    while cur:
        print(cur.val)
        cur = cur.next


if __name__ == '__main__':
    node = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    show(node)
    print('---')
    new_node = reverse(node)
    show(new_node)

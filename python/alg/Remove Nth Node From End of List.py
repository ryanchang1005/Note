"""
Remove Nth Node From End of List
移除LinkedList最後第N個Node

思路
    用兩個指標pre, cur, 都先指到head
    cur先往前N個, 如cur遇到null, 則直接移除head.next
    LOOP 直到cur遇到null, 停止
    移除pre下一個
    
    head
    '1'  >  '2'  >  '3'  >  '4'  >  NULL
    pre             cur

    head
    '1'  >  '2'  >  '3'  >  '4'  >  NULL
            pre             cur

    head
    '1'  >  '2'      >      '4'  >  NULL

"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        cur = self
        txt = ''
        while cur:
            if len(txt) == 0:
                txt += f'{cur.val}'
            else:
                txt += f', {cur.val}'
            cur = cur.next
        return f'[{txt}]'


def run(node, n):
    # init
    pre = node
    cur = node

    # move n
    for i in range(n):
        cur = cur.next

    while cur.next:
        pre = pre.next
        cur = cur.next

    # remove
    pre.next = pre.next.next
    return node


if __name__ == '__main__':
    print(run(Node(1, Node(2, Node(3, Node(4)))), 2))  # [1, 2, 4]

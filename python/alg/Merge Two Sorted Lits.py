"""
Merge Two Sorted List
Input:
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

recursively
    merge(a, b):
        # 停止, 當a或b其中一個為None, 則返回不為None的那一個
        if not a or not b:
            return a or b

        if a < b:
            a.next = merge(a.next, b)  # 因為a小, 所以a.next就交給下一層決定, 並把"a後面"的和"b"丟給下一層判斷
            return a  # 如果以第一層來看, 回傳a, 因為此值一定最小
        else: # 一樣或 a > b, 反之
            b.next = merge(a, b.next)
            return b

iteratively
    run(a, b):
        head = cur  # 鎖住起始node用, 初始Node(0)為暫存用, 實際答案為head.next
        cur = Node(0)  # 存結果用指標, 會不斷往後推
        while a and b: # 直到a或b其中一個為None才停
            if a < b:
                cur存a, 並推進a
            else:
                反之
            推進cur
        cur存a或b, 看誰有值存誰
        return head.next
    
Time complex: O(len(a) + len(b))
Space complex: O(len(a) + len(b))
"""


class Node:
    def __init__(self, val, next):
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


class RecursivelySolve:
    def run(self, l, r):
        if not l or not r:
            return l or r

        if l.val < r.val:
            l.next = self.run(l.next, r)
            return l
        else:
            r.next = self.run(l, r.next)
            return r


class IterativelySolve:
    def run(self, l, r):
        cur = Node(0, None)
        head = cur
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return head.next


if __name__ == '__main__':
    ret = RecursivelySolve().run(
        Node(1, Node(2, Node(4, None))),
        Node(1, Node(3, Node(4, None)))
    )
    print(f'RecursivelySolve : {str(ret)}')

    ret = IterativelySolve().run(
        Node(1, Node(2, Node(4, None))),
        Node(1, Node(3, Node(4, None)))
    )
    print(f'IterativelySolve : {str(ret)}')

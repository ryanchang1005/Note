"""
Merge k Sorted Lists
合併多個排序過的List

Input: lists = [
    [1,4,5],
    [1,3,4],
    [2,6]
]
Output: [1,1,2,3,4,4,5,6]

需用divide and conquer不然會超時
index (0, 3), (1, 4), (2, 5)先合併再來(0, 2)再來(0, 1)

在猜如果是(0,1), (0,2), (0,3), (0,4), (0,5)這樣合併的話0會過長導致超時??
divide and conquer的話每個是均等增加
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


def mergeKList(lists):
    if len(lists) == 0:
        return None

    if len(lists) == 1:
        return lists[0]

    mid = int(len(lists) / 2)
    l = mergeKList(lists[:mid])
    r = mergeKList(lists[mid:])
    return RecursivelySolve().run(l, r)


if __name__ == '__main__':
    ret = mergeKList([
        Node(1, Node(4, Node(5))),
        Node(1, Node(3, Node(4))),
        Node(2, Node(6)),
    ])
    print(str(ret))

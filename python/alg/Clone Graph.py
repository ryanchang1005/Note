"""
Clone Graph
複製一個無向圖

DFS - recursively
    利用map, 先將當前節點放到map(節點:新節點)(node: Node(node.val))複製
    遍歷neighbors
        如該neighbor不再map中:
            加到map
            dfs
        將當前node的neighbors.add(此neighbor)

DFS - iteratively
    用stack
    # stack.append(it)
    # stack.pop()
    
BFS
    用queue, 左進右出
    # l.insert(0, it)
    # l.pop()

結構都差不多只差在用, dfs, stack.append(it), l.insert(0, it)
"""


class Node:
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class DFSWithRecursivelySolve:

    def run(self, node):
        if not node:
            return None

        m = {node: Node(node.val)}

        def dfs(node, m):
            for neighbor in node.neighbors:
                if neighbor not in m:
                    m[neighbor] = Node(neighbor.val)
                    dfs(neighbor, m)
                m[node].neighbors.append(m[neighbor])

        dfs(node, m)
        return m[node]


class DFSWithIterativelySolve:

    def run(self, node):
        if not node:
            return None

        m = {node: Node(node.val)}
        # stack.append(it)
        # stack.pop()
        stack = [node]

        while len(stack) != 0:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in m:
                    m[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                m[n].neighbors.append(m[neighbor])

        return m[node]


class BFSSolve:

    def run(self, node):
        if not node:
            return None

        m = {node: Node(node.val)}
        # l.insert(0, it)
        # l.pop()
        l = [node]

        while len(l) != 0:
            n = l.pop()
            for neighbor in n.neighbors:
                if neighbor not in m:
                    m[neighbor] = Node(neighbor.val)
                    l.insert(0, neighbor)
                m[n].neighbors.append(m[neighbor])

        return m[node]

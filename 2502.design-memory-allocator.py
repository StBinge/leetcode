#
# @lc app=leetcode.cn id=2502 lang=python3
# @lcpr version=30204
#
# [2502] 设计内存分配器
#
from sbw import *
from sortedcontainers import SortedList

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class LinkNode:
    def __init__(self, idx, size, used) -> None:
        self.idx = idx
        self.size = size
        self.prev: Optional[LinkNode] = None
        self.next: Optional[LinkNode] = None
        self.used = used

    def __repr__(self) -> str:
        return str((self.idx, self.size, self.used))


class Allocator:

    def __init__(self, n: int):
        self.root = LinkNode(-1, 1, True)
        free = LinkNode(0, n, False)
        self.root.next = free
        free.prev = self.root
        self.free = {0: free}
        self.used = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        for idx in sorted(self.free.keys()):
            if self.free[idx].size < size:
                continue
            node = self.free.pop(idx)
            node.used = True
            self.used[mID].append(node)
            if node.size != size:
                remain = node.size - size
                node.size = size
                nxt_free = LinkNode(node.idx + size, remain, False)
                nxt_free.prev = node
                nxt_free.next = node.next
                if nxt_free.next:
                    nxt_free.next.prev=nxt_free
                node.next = nxt_free

                self.free[nxt_free.idx] = nxt_free              
            return node.idx
        return -1

    def free_node(self, node: LinkNode):
        size = node.size
        node.used = False
        if node.prev.used == False:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            node = node.prev
            node.size += size
        if node.next and node.next.used == False:
            self.free.pop(node.next.idx)
            node.size += node.next.size
            node.next = node.next.next
            if node.next:
                node.next.prev = node

        self.free[node.idx] = node
        return size

    def freeMemory(self, mID: int) -> int:
        if mID not in self.used:
            return 0
        nodes = self.used.pop(mID)
        tot_size = 0
        for node in nodes:
            tot_size += self.free_node(node)
        return tot_size


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
# @lc code=end
def display(root: LinkNode):
    ret = []
    while root:
        ret.append([root.idx, root.size, root.used])
        root = root.next
    return ret
    print(ret)

def assert_node(node:LinkNode):
    if not node.next:
        return
    assert node==node.next.prev,'Invalid link:'+str(node)
    assert node.idx+node.size==node.next.idx,'invalid node next'
    assert_node(node.next)

test_obj(
    Allocator,
    [
        "Allocator",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "allocate",
        "allocate",
        "allocate",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "allocate",
        "allocate",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "allocate",
        "allocate",
        "freeMemory",
        "allocate",
        "allocate",
        "allocate",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "allocate",
        "freeMemory",
        "allocate",
        "freeMemory",
        "allocate",
        "allocate",
        "freeMemory",
        "allocate",
        "allocate",
        "freeMemory",
        "freeMemory",
        "allocate",
        "freeMemory",
        "freeMemory",
        "allocate",
        "allocate",
        "allocate",
        "freeMemory",
        "allocate",
        "allocate",
        "freeMemory",
        "freeMemory",
        "allocate",
        "allocate",
        "allocate",
        "freeMemory",
        "allocate",
        "allocate",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "allocate",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "freeMemory",
        "allocate",
        "allocate",
        "allocate",
        "freeMemory",
        "allocate",
        "freeMemory",
        "freeMemory",
        "allocate",
        "freeMemory",
        "allocate",
        "freeMemory",
        "freeMemory",
    ],
    [
        [100],
        [27],
        [12],
        [53],
        [61],
        [80],
        [21, 78],
        [81, 40],
        [50, 76],
        [40],
        [76],
        [63],
        [25, 100],
        [96, 12],
        [92],
        [92],
        [84],
        [19, 71],
        [22, 90],
        [60],
        [42, 79],
        [26, 41],
        [59, 33],
        [79],
        [58],
        [97],
        [92],
        [97],
        [92],
        [40],
        [52, 74],
        [40],
        [53, 17],
        [17],
        [36, 32],
        [51, 13],
        [41],
        [5, 87],
        [44, 66],
        [71],
        [53],
        [74, 14],
        [78],
        [14],
        [32, 54],
        [45, 28],
        [84, 47],
        [16],
        [100, 78],
        [5, 99],
        [33],
        [100],
        [62, 79],
        [31, 32],
        [85, 81],
        [78],
        [34, 45],
        [47, 7],
        [7],
        [84],
        [6],
        [35, 55],
        [94],
        [87],
        [20],
        [87],
        [96, 60],
        [40, 66],
        [28, 96],
        [28],
        [25, 2],
        [100],
        [96],
        [19, 35],
        [16],
        [92, 42],
        [80],
        [79],
    ],
    "[null,0,0,0,0,0,0,-1,21,0,50,0,21,-1,0,0,0,46,65,0,-1,-1,-1,0,0,0,0,0,0,0,-1,0,-1,0,-1,-1,0,87,-1,19,0,-1,21,0,-1,-1,-1,0,-1,0,0,25,-1,5,-1,0,-1,-1,0,0,0,-1,0,5,0,0,-1,-1,36,0,-1,0,28,36,0,-1,0,0]",
)
test_obj(
    Allocator,
    [
        "Allocator",
        "allocate",
        "allocate",
        "allocate",
        "freeMemory",
        "allocate",
        "allocate",
        "allocate",
        "freeMemory",
        "allocate",
        "freeMemory",
    ],
    [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]],
    "[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]",
)

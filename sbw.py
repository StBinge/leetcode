from typing import List,Optional
from collections import deque,Counter,defaultdict
from functools import cache
from itertools import accumulate
from random import randint
from bisect import bisect,bisect_left,bisect_right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build(cls, nums: list) -> "ListNode":
        dummy = ListNode(0)
        cur = dummy
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next

    def to_list(self):
        cur = self
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return nums
    def print(self):      

        print("->".join(map(str, self.to_list())))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def build(cls, vals):
        if isinstance(vals, str):
            vals = eval(vals.replace("null", "None"))
        if not vals:
            return None
        root = TreeNode(vals[0])
        queue = [root]
        idx = 1
        N = len(vals)
        while queue and idx < N:
            temp = []
            for node in queue:
                if idx == N:
                    break
                node.left = TreeNode(vals[idx]) if vals[idx] != None else None
                if node.left:
                    temp.append(node.left)
                idx += 1
                if idx == N:
                    break
                node.right = TreeNode(vals[idx]) if vals[idx] != None else None
                if node.right:
                    temp.append(node.right)
                idx += 1
            queue = temp
        return root

    def to_str(self):
        if not self:
            return "[null]"
        queue = [self]
        ret = []
        while queue:
            nxt = []
            for node in queue:
                if not node:
                    ret.append(None)
                else:
                    ret.append(node.val)
                    nxt.append(node.left)
                    nxt.append(node.right)
            queue = nxt
        while ret and ret[-1] == None:
            ret.pop()
        return "[" + ",".join(map(str, ret)).replace("None", "null") + "]"

    def print(self):
        print(self.to_str())


class SortedSet:
    def __init__(self) -> None:
        self.array = []
        self.set = set()

    def add(self, value):
        if value in self.set:
            return
        self.set.add(value)
        self.array.insert(self.bisect_right(value), value)

    def bisect_right(self, value):
        left, right = 0, len(self.array)
        while left < right:
            mid = (left + right) // 2
            x = self.array[mid]
            if x < value:
                left = mid + 1
            else:
                right = mid
        return left

    def bisect_left(self, value):
        left, right = 0, len(self.array)
        x = 0
        while left < right:
            mid = (left + right) // 2
            x = self.array[mid]
            if x > value:
                right = mid
            else:
                left = mid + 1
        return left - 1


def format_array(s: str):
    s = s.replace("null", "None")
    return eval(s)


def eval_list_str(s: str):
    replace_items = [
        ["null", "None"],
        ["false", "False"],
        ["true", "True"],
    ]
    for old, new in replace_items:
        s = s.replace(old, new)
    return eval(s)


def exec_expression(expr: str):
    import re

    expr = re.sub(r",\s+", "\n", expr)
    old_vars=locals().copy()

    exec(expr)
    ret={}
    for k,v in locals().items():
        if k not in old_vars:
            ret[k]=v
    ret.pop('old_vars')
    ret.pop('ret')
    return ret

if __name__ == "__main__":
    r = exec_expression("grid = [[1,1],[1,2]], row = 0, col = 0, color = 3")
    pass

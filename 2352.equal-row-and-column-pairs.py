#
# @lc app=leetcode.cn id=2352 lang=python3
# @lcpr version=30204
#
# [2352] 相等行列对
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.slots = {}
        self.cnt=0

    def insert(self, values):
        cur = self
        for v in values:
            cur = cur.slots.setdefault(v, Trie())
        cur.cnt+=1

    def query(self, values):
        cur = self
        for v in values:
            cur = cur.slots.get(v, None)
            if not cur:
                return 0
        return cur.cnt


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        root = Trie()
        for row in grid:
            root.insert(row)

        ret = 0
        for col in zip(*grid):
            ret += root.query(col)
        return ret


# @lc code=end
assert Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
assert Solution().equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1


#
# @lcpr case=start
# [[3,2,1],[1,7,6],[2,7,7]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]\n
# @lcpr case=end

#

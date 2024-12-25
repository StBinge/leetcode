#
# @lc app=leetcode.cn id=2136 lang=python3
# @lcpr version=30204
#
# [2136] 全部开花的最早一天
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class SegNode:
    def __init__(self, n) -> None:
        self.vals = [0] * (n + 1)
        self.n = n

    def add(self, x):
        while x <= self.n:
            self.vals[x] += 1
            x += x & -x

    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.vals[x]
            x -= x & -x
        return ret


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        N = len(plantTime)
        sorted_idx = sorted(range(N), key=growTime.__getitem__, reverse=True)
        ret = 0
        day = 0
        for idx in sorted_idx:
            day += plantTime[idx]
            ret = max(ret, growTime[idx]+day)
        return ret


# @lc code=end
assert Solution().earliestFullBloom(plantTime=[1], growTime=[1]) == 2
assert Solution().earliestFullBloom(plantTime=[1, 2, 3, 2], growTime=[2, 1, 2, 1]) == 9
assert Solution().earliestFullBloom(plantTime=[1, 4, 3], growTime=[2, 3, 1]) == 9


#
# @lcpr case=start
# [1,4,3]\n[2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,2]\n[2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1]\n
# @lcpr case=end

#

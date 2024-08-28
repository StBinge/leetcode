#
# @lc app=leetcode.cn id=1936 lang=python3
# @lcpr version=30204
#
# [1936] 新增的最少台阶数
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        # N = len(rungs)
        prev = 0
        ret=0
        for h in rungs:
            d=h-prev
            ret+=(d-1)//dist
            prev=h
        return ret


# @lc code=end

assert Solution().addRungs(rungs=[5], dist=10) == 0
assert Solution().addRungs(rungs=[3, 4, 6, 7], dist=2) == 1
assert Solution().addRungs(rungs=[3, 6, 8, 10], dist=3) == 0
assert Solution().addRungs(rungs=[1, 3, 5, 10], dist=2) == 2

#
# @lcpr case=start
# [1,3,5,10]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,6,8,10]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,4,6,7]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5]\n10\n
# @lcpr case=end

#

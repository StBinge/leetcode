#
# @lc app=leetcode.cn id=2731 lang=python3
# @lcpr version=30204
#
# [2731] 移动机器人
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for i, dir in enumerate(s):
            nums[i] += d * (1 if dir == "R" else -1)

        nums.sort()
        ret = 0
        pre = 0
        for i in range(1, len(nums)):
            pre =(pre+ i * (nums[i] - nums[i - 1]))%(10**9+7)
            ret =(ret+pre)%(10**9+7)
        return ret


# @lc code=end

assert Solution().sumDistance([-10,-13,10,14,11],"LRLLR",2) == 146
assert Solution().sumDistance(nums=[1, 0], s="RL", d=2) == 5
assert Solution().sumDistance(nums=[-2, 0, 2], s="RLL", d=3) == 8

#
# @lcpr case=start
# [-2,0,2]\n"RLL"\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0]\n"RL"\n2\n
# @lcpr case=end

#

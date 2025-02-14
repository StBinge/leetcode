#
# @lc app=leetcode.cn id=2860 lang=python3
# @lcpr version=30204
#
# [2860] 让所有学生保持开心的分组方法数
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ret = int(nums[0] > 0)
        for i, (x, y) in enumerate(pairwise(nums), 1):
            if x < i < y:
                ret += 1
        ret += 1
        return ret


# @lc code=end

assert Solution().countWays([6, 0, 3, 3, 6, 7, 2, 7]) == 3
assert Solution().countWays([1, 1, 0, 1]) == 1
assert Solution().countWays([1, 1]) == 2

#
# @lcpr case=start
# [1,1]\n
# @lcpr case=end

# @lcpr case=start
# [6,0,3,3,6,7,2,7]\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=3423 lang=python3
# @lcpr version=30204
#
# [3423] 循环数组中相邻元素的最大差值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[0]-nums[-1]),max(abs(x-y) for x,y in pairwise(nums)))
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-5,-10,-5]\n
# @lcpr case=end

#


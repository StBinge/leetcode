#
# @lc app=leetcode.cn id=2221 lang=python3
# @lcpr version=30204
#
# [2221] 数组的三角和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N=len(nums)
        for j in range(N-1):
            for i in range(N-j-1):
                nums[i]=(nums[i]+nums[i+1])%10
        return nums[0]
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [5]\n
# @lcpr case=end

#


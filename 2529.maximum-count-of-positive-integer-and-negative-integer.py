#
# @lc app=leetcode.cn id=2529 lang=python3
# @lcpr version=30204
#
# [2529] 正整数和负整数的最大计数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg=-1
        pos=len(nums)
        for i,n in enumerate(nums):
            if n<0:
                neg=i
            elif n>0:
                pos=i
                break
        return max(neg+1,len(nums)-pos)

# @lc code=end



#
# @lcpr case=start
# [-2,-1,-1,1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-3,-2,-1,0,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,20,66,1314]\n
# @lcpr case=end

#


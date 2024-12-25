#
# @lc app=leetcode.cn id=2778 lang=python3
# @lcpr version=30204
#
# [2778] 特殊元素平方和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ret=0
        N=len(nums)
        for i,n in enumerate(nums,1):
            if N%i==0:
                ret+=n*n
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,1,19,18,3]\n
# @lcpr case=end

#


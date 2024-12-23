#
# @lc app=leetcode.cn id=面试题 17.04 lang=python3
# @lcpr version=30204
#
# [面试题 17.04] 消失的数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from operator import xor
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N=len(nums)+1
        if N%4==0:
            x=0
        elif N%4==1:
            x=N-1
        elif N%4==2:
            x=1
        else:
            x=N
        ret= reduce(xor,nums,x)
        return ret
# @lc code=end

assert Solution().missingNumber([3,0,1])==2

#
# @lcpr case=start
# [3,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [9,6,4,2,3,5,7,0,1]\n
# @lcpr case=end

#


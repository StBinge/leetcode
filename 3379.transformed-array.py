#
# @lc app=leetcode.cn id=3379 lang=python3
# @lcpr version=30204
#
# [3379] 转换数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N=len(nums)
        ret=[0]*N
        for i,n in enumerate(nums):
            ret[i]=nums[(i+n)%N]
        return ret
# @lc code=end



#
# @lcpr case=start
# [3,-2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [-1,4,-1]\n
# @lcpr case=end

#


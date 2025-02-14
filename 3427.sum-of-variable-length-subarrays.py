#
# @lc app=leetcode.cn id=3427 lang=python3
# @lcpr version=30204
#
# [3427] 变长子数组求和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        N=len(nums)
        difs=[0]*(N+1)
        for i,n in enumerate(nums):
            start=max(0,i-n)
            difs[start]+=1
            difs[i+1]-=1
        ret=0
        mul=0
        for i in range(N):
            mul+=difs[i]
            ret+=mul*nums[i]
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,1,2]\n
# @lcpr case=end

#


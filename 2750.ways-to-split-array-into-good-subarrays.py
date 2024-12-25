#
# @lc app=leetcode.cn id=2750 lang=python3
# @lcpr version=30204
#
# [2750] 将数组划分成若干好子数组的方式
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        N=len(nums)
        left=0
        while left<N and nums[left]==0:
            left+=1
        if left==N:
            return 0
        right=N-1
        while right>left and nums[right]==0:
            right-=1
        if left==right:
            return 1
        
        zeros=0
        ret=1
        for i in range(left,right+1):
            if nums[i]==0:
                zeros+=1
            else:
                ret=ret*(zeros+1)%(10**9+7)
                zeros=0
        return ret
        
# @lc code=end
assert Solution().numberOfGoodSubarraySplits([0,1,0,0,1])==3


#
# @lcpr case=start
# [0,1,0,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

#


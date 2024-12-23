#
# @lc app=leetcode.cn id=2367 lang=python3
# @lcpr version=30204
#
# [2367] 等差三元组的数目
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        N=len(nums)
        j,k=1,2
        ret=0
        for i in range(N):
            while j<N and nums[j]<nums[i]+diff:
                j+=1
            if j==N:
                return ret
            while k<N and nums[k]<nums[j]+diff:
                k+=1
            if k==N:
                return ret
            if nums[k]-nums[j]==diff and nums[j]-nums[i]==diff:
                ret+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [0,1,4,6,7,10]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,8,9]\n2\n
# @lcpr case=end

#


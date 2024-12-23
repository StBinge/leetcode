#
# @lc app=leetcode.cn id=2233 lang=python3
# @lcpr version=30204
#
# [2233] K 次增加后的最大乘积
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums.sort()
        Mod=10**9+7
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            dif=nums[i+1]-nums[i]
            if k>=(i+1)*dif:
                k-=(i+1)*dif
                continue
            x,y=divmod(k,i+1)
            return reduce(lambda x,y:x*y%Mod,nums[i+1:])*pow(nums[i]+x,i+1-y,Mod)*pow(nums[i]+x+1,y,Mod)%Mod
        N=len(nums)
        x,y=divmod(k,N)
        return pow(nums[-1]+x,N-y,Mod)*pow(nums[-1]+x+1,y,Mod)%Mod
# @lc code=end
assert Solution().maximumProduct(nums = [6,3,3,2], k = 2)==216
assert Solution().maximumProduct(nums = [0,4], k = 5)==20


#
# @lcpr case=start
# [0,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [6,3,3,2]\n2\n
# @lcpr case=end

#


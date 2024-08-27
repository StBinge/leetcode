#
# @lc app=leetcode.cn id=2012 lang=python3
# @lcpr version=30204
#
# [2012] 数组美丽值求和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        N=len(nums)
        right_min=[0]*N
        right_min[-1]=nums[-1]
        for i in range(N-2,-1,-1):
            right_min[i]=min(nums[i],right_min[i+1])
        ret=0
        left_max=nums[0]
        for i in range(1,N-1):
            if left_max<nums[i]<right_min[i+1]:
                ret+=2
            elif nums[i-1]<nums[i]<nums[i+1]:
                ret+=1
            left_max=max(nums[i],left_max)
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#


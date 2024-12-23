#
# @lc app=leetcode.cn id=3010 lang=python3
# @lcpr version=30204
#
# [3010] 将数组分成最小总代价的子数组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        m1,m2=nums[1],nums[2]
        if m1>m2:
            m1,m2=m2,m1
        
        for i in range(3,len(nums)):
            if nums[i]<m1:
                m1,m2=nums[i],m1
            elif nums[i]<m2:
                m2=nums[i]
        return nums[0]+m1+m2

# @lc code=end



#
# @lcpr case=start
# [1,2,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [10,3,1,1]\n
# @lcpr case=end

#


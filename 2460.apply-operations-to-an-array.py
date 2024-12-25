#
# @lc app=leetcode.cn id=2460 lang=python3
# @lcpr version=30204
#
# [2460] 对数组执行操作
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        idx=0
        for i in range(len(nums)-1):
            if nums[i]==0:
                continue
            if nums[i]==nums[i+1]:
                nums[idx]=nums[i]*2
                nums[i+1]=0
            else:
                nums[idx]=nums[i]
            idx+=1
        nums[idx]=nums[-1]
        idx+=1
        for i in range(idx,len(nums)):
            nums[i]=0
        return nums

# @lc code=end



#
# @lcpr case=start
# [1,2,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

#


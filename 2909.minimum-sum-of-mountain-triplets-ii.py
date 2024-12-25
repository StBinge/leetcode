#
# @lc app=leetcode.cn id=2909 lang=python3
# @lcpr version=30204
#
# [2909] 元素和最小的山形三元组 II
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        N=len(nums)
        
        ret=float('inf')
        min_left=[nums[0]]
        for i in range(1,N):
            min_left.append(min(min_left[-1],nums[i]))
        right_min=nums[-1]
        for i in range(len(nums)-2,0,-1):
            if nums[i]>min_left[i] and nums[i]>right_min:
                ret=min(ret,nums[i]+min_left[i]+right_min)
            right_min=min(right_min,nums[i])
        
            
        return ret if ret<float('inf') else -1
# @lc code=end
assert Solution().minimumSum([5,4,8,7,10,2])==13
assert Solution().minimumSum([8,6,1,5,3])==9


#
# @lcpr case=start
# [8,6,1,5,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,7,10,2]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,4,3,4,5]\n
# @lcpr case=end

#


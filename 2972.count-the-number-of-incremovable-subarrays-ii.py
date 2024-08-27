#
# @lc app=leetcode.cn id=2972 lang=python3
# @lcpr version=30204
#
# [2972] 统计移除递增子数组的数目 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        left=0
        N=len(nums)
        while left+1<N and nums[left]<nums[left+1]:
            left+=1
        if left==N-1:
            return (N+1)*N//2
        
        ret=left+2
        right=N-1
        while right==N-1 or nums[right]<nums[right+1]:
            while left>=0 and nums[left]>=nums[right]:
                left-=1
            ret+=left+2
            right-=1
        return ret
# @lc code=end

assert Solution().incremovableSubarrayCount([6,5,7,8])==7
assert Solution().incremovableSubarrayCount([1,2,3,4])==10

#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,7,8]\n
# @lcpr case=end

# @lcpr case=start
# [8,7,6,6]\n
# @lcpr case=end

#


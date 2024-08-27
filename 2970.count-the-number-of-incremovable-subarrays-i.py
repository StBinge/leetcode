#
# @lc app=leetcode.cn id=2970 lang=python3
# @lcpr version=30204
#
# [2970] 统计移除递增子数组的数目 I
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        N = len(nums)
        i=0
        while i<N-1 and nums[i]<nums[i+1]:
            i+=1
        if i==N-1:
            return (N+1)*N//2
        
        ans=i+2
        j=N-1
        while j==N-1 or nums[j]<nums[j+1]:
            while i>=0 and nums[i]>=nums[j]:
                i-=1
            ans+=i+2
            j-=1
        return ans


# @lc code=end
assert Solution().incremovableSubarrayCount([2,1,1,4]) == 5
assert Solution().incremovableSubarrayCount([6,5,7,8]) == 7
assert Solution().incremovableSubarrayCount([1, 2, 3, 4]) == 10


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

#
# @lc app=leetcode.cn id=3107 lang=python3
# @lcpr version=30204
#
# [3107] 使数组中位数等于 K 的最少操作数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        mid=N//2
        ret=0
        if nums[mid]>k:
            for i in range(mid,-1,-1):
                if nums[i]<=k:
                    break
                ret+=nums[i]-k
        else:
            for i in range(mid,N):
                if nums[i]>=k:
                    break
                ret+=k-nums[i]
        return ret
        


# @lc code=end
assert Solution().minOperationsToMakeMedianK([98, 52], 82) == 16
assert Solution().minOperationsToMakeMedianK([75, 17, 74, 22, 40, 86], 86) == 23
assert Solution().minOperationsToMakeMedianK(nums=[1, 2, 3, 4, 5, 6], k=4) == 0
assert Solution().minOperationsToMakeMedianK(nums=[2, 5, 6, 8, 5], k=7) == 3
assert Solution().minOperationsToMakeMedianK(nums=[2, 5, 6, 8, 5], k=4) == 2


#
# @lcpr case=start
# [2,5,6,8,5]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,5,6,8,5]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n4\n
# @lcpr case=end

#

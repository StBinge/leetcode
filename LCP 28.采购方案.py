#
# @lc app=leetcode.cn id=LCP 28 lang=python3
# @lcpr version=30204
#
# [LCP 28] 采购方案
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        if min(nums)>target:
            return 0
        nums.sort()

        idx=len(nums)-1
        ret=0
        for i,n in enumerate(nums):
            while idx>=0 and nums[idx]+n>target:
                idx-=1
            if idx<=i:
                break
            ret+=idx-i
            ret%=10**9+7
        return ret

# @lc code=end
assert Solution().purchasePlans( [2,2,1,9],10)==4
assert Solution().purchasePlans([2,5,3,5],6)==1


#
# @lcpr case=start
# [2,5,3,5]\n6`>\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,9]\n10`>\n
# @lcpr case=end

#


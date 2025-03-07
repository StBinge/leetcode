#
# @lc app=leetcode.cn id=3315 lang=python3
# @lcpr version=30204
#
# [3315] 构造最小位运算数组 II
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i,n in enumerate(nums):
            if n&1==0:
                nums[i]=-1
                continue
            t=~n
            nums[i]^=(t&-t)>>1
        return nums

# @lc code=end
assert Solution().minBitwiseArray( [11,13,31])==[9,12,15]
assert Solution().minBitwiseArray([2,3,5,7])==[-1,1,4,3]


#
# @lcpr case=start
# [2,3,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,31]\n
# @lcpr case=end

#


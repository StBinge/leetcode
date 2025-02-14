#
# @lc app=leetcode.cn id=3095 lang=python3
# @lcpr version=30204
#
# [3095] 或值至少 K 的最短子数组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ret = float('inf')
        left=bottom=right_or=0
        for right,x in enumerate(nums):
            right_or|=x
            while left<=right and nums[left]|right_or>=k:
                ret=min(ret,right-left+1)
                left+=1
                if left>bottom:
                    for i in range(right-1,left-1,-1):
                        nums[i]|=nums[i+1]
                    right_or=0
                    bottom=right
        return ret if ret<float('inf') else -1

                


# @lc code=end
assert Solution().minimumSubarrayLength([1],0)==1
assert Solution().minimumSubarrayLength([1,2,3],2)==1
assert Solution().minimumSubarrayLength([2,1,8],10)==3


#
# @lcpr case=start
# [1,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,1,8]\n10\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

#


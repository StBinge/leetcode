#
# @lc app=leetcode.cn id=2202 lang=python3
# @lcpr version=30204
#
# [2202] K 次操作后最大化顶端元素
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums)==1 and k&1:
            return -1
        return max(nums[i] for i in range(min(k+1,len(nums))) if i<k-1 or i==k)


# @lc code=end
assert Solution().maximumTop([2,5,6,2,10,18,14,7,3,0,18,15], 6) == 14
assert Solution().maximumTop([3, 2, 1], 1) == 2
assert Solution().maximumTop([18], 3) == -1
assert Solution().maximumTop([91, 98, 17, 79, 15, 55, 47, 86, 4, 5], 2) == 91
assert Solution().maximumTop(nums=[2], k=1) == -1
assert Solution().maximumTop(nums=[5, 2, 2, 4, 0, 6], k=4) == 5


#
# @lcpr case=start
# [5,2,2,4,0,6]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

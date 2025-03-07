#
# @lc app=leetcode.cn id=3397 lang=python3
# @lcpr version=30204
#
# [3397] 执行操作后不同元素的最大数量
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if 2*k+1 > len(nums):
            return len(nums)
        nums.sort()
        mi = float("-inf")
        ret=0
        for n in nums:
            x=min(max(n-k,mi+1),n+k)
            if x>mi:
                ret+=1
                mi=x
        return ret


# @lc code=end
assert Solution().maxDistinctElements([9,10,9,9,9],1) == 4
assert Solution().maxDistinctElements(nums=[9,9,10,10], k=1) == 4
assert Solution().maxDistinctElements(nums=[9, 5, 5], k=0) == 2
assert Solution().maxDistinctElements(nums=[4, 4, 4, 4], k=1) == 3
assert Solution().maxDistinctElements(nums=[1, 2, 2, 3, 3, 4], k=2) == 6


#
# @lcpr case=start
# [1,2,2,3,3,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,4,4,4]\n1\n
# @lcpr case=end

#

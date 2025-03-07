#
# @lc app=leetcode.cn id=3282 lang=python3
# @lcpr version=30204
#
# [3282] 到达数组末尾的最大得分
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ans=mx=0
        for n in nums[:-1]:
            mx=max(mx,n)
            ans+=mx
        return ans



# @lc code=end
assert Solution().findMaximumScore([3,1,8,10]) == 14
assert Solution().findMaximumScore([1]) == 0
assert Solution().findMaximumScore([4,3,1,3,2]) == 16
assert Solution().findMaximumScore([1, 3, 1, 5]) == 7


#
# @lcpr case=start
# [1,3,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,1,3,2]\n
# @lcpr case=end

#

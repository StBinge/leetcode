#
# @lc app=leetcode.cn id=2733 lang=python3
# @lcpr version=30204
#
# [2733] 既不是最小值也不是最大值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return sorted(nums[:3])[1] if len(nums)>2 else -1
        
# @lc code=end

assert Solution().findNonMinOrMax([2,4,25])==4
assert Solution().findNonMinOrMax([1,2]) not in [1,2]
assert Solution().findNonMinOrMax([3,2,1,4]) not in [1,4]

#
# @lcpr case=start
# [3,2,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

#


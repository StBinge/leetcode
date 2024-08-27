#
# @lc app=leetcode.cn id=2740 lang=python3
# @lcpr version=30204
#
# [2740] 找出分区值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(y-x for x,y in pairwise(nums))
# @lc code=end
assert Solution().findValueOfPartition([1,3,2,4])==1
assert Solution().findValueOfPartition([100,1,10])==9


#
# @lcpr case=start
# [1,3,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [100,1,10]\n
# @lcpr case=end

#


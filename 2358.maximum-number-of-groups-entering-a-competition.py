#
# @lc app=leetcode.cn id=2358 lang=python3
# @lcpr version=30204
#
# [2358] 分组的最大数量
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return int(math.sqrt(2*len(grades)+0.25)-.5)

# @lc code=end
assert Solution().maximumGroups([8,8])==1
assert Solution().maximumGroups([10,6,12,7,3,5])==3


#
# @lcpr case=start
# [10,6,12,7,3,5]\n
# @lcpr case=end

# @lcpr case=start
# [8,8]\n
# @lcpr case=end

#


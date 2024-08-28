#
# @lc app=leetcode.cn id=1953 lang=python3
# @lcpr version=30204
#
# [1953] 你可以工作的最大周数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        mx=max(milestones)
        s=sum(milestones)-mx
        if mx<=s:
            return s+mx
        else:
            return s*2+1
        
# @lc code=end

assert Solution().numberOfWeeks([5,2,1])==7
assert Solution().numberOfWeeks([1,2,3])==6

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,2,1]\n
# @lcpr case=end

#


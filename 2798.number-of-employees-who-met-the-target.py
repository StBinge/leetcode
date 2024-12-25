#
# @lc app=leetcode.cn id=2798 lang=python3
# @lcpr version=30204
#
# [2798] 满足目标工作时长的员工数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(h>=target for h in hours)
# @lc code=end



#
# @lcpr case=start
# [0,1,2,3,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,2,2]\n6\n
# @lcpr case=end

#


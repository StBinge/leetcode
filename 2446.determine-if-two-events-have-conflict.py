#
# @lc app=leetcode.cn id=2446 lang=python3
# @lcpr version=30204
#
# [2446] 判断两个事件是否存在冲突
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0]<=event2[1] and event2[0]<=event1[1]

# @lc code=end



#
# @lcpr case=start
# ["01:15","02:00"]\n["02:00","03:00"]\n
# @lcpr case=end

# @lcpr case=start
# ["01:00","02:00"]\n["01:20","03:00"]\n
# @lcpr case=end

# @lcpr case=start
# ["10:00","11:00"]\n["14:00","15:00"]\n
# @lcpr case=end

#


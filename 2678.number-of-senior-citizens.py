#
# @lc app=leetcode.cn id=2678 lang=python3
# @lcpr version=30204
#
# [2678] 老人的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # ret=0
        # for d in details:
        #     ret+=int(d[11:13])>60
        return sum(int(d[11:13])>60 for d in details)
# @lc code=end



#
# @lcpr case=start
# ["7868190130M7522","5303914400F9211","9273338290F4010"]\n
# @lcpr case=end

# @lcpr case=start
# ["1313579440F2036","2921522980M5644"]\n
# @lcpr case=end

#


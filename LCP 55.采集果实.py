#
# @lc app=leetcode.cn id=LCP 55 lang=python3
# @lcpr version=30204
#
# [LCP 55] 采集果实
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        ret=0
        for t,n in fruits:
            ret+=((n-1)//limit+1)*time[t]
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,3,2]\n[[0,2],[1,4],[2,1]]\n3`>\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[[0,3],[0,5]]\n2`>\n
# @lcpr case=end

#


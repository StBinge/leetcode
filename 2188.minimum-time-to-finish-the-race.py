#
# @lc app=leetcode.cn id=2188 lang=python3
# @lcpr version=30204
#
# [2188] 完成比赛的最少时间
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        N=len(tires)
        mi_ft=min(t[0] for t in tires)
        target=mi_ft+changeTime
        can_use=[]
        for f,r in tires:
            cnt=0
            


# @lc code=end



#
# @lcpr case=start
# [[2,3],[3,4]]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [[1,10],[2,2],[3,4]]\n6\n5\n
# @lcpr case=end

#


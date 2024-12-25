#
# @lc app=leetcode.cn id=LCP 39 lang=python3
# @lcpr version=30204
#
# [LCP 39] 无人机方阵
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        cnt=defaultdict(int)
        for srow,trow in zip(source,target):
            for scol,tcol in zip(srow,trow):
                cnt[scol]+=1
                cnt[tcol]-=1
        return sum(v for v in cnt.values() if v>0)
# @lc code=end



#
# @lcpr case=start
# [[1,3],[5,4]]\n[[3,1],[6,5]]`>\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[3,4,5]]\n[[1,3,5],[2,3,4]]`>\n
# @lcpr case=end

#


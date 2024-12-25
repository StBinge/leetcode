#
# @lc app=leetcode.cn id=LCP 66 lang=python3
# @lcpr version=30204
#
# [LCP 66] 最小展台数量
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        cnt=defaultdict(int)
        for day in demand:
            c=Counter(day)
            for k,v in c.items():
                cnt[k]=max(cnt[k],v)
        return sum(cnt.values())
# @lc code=end



#
# @lcpr case=start
# ["acd","bed","accd"]`>\n
# @lcpr case=end

# @lcpr case=start
# ["abc","ab","ac","b"]`>\n
# @lcpr case=end

#


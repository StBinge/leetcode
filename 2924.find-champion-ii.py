#
# @lc app=leetcode.cn id=2924 lang=python3
# @lcpr version=30204
#
# [2924] 找到冠军 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_deg=[False]*n
        for u,v in edges:
            in_deg[v]=True
        ret=-1
        for i,f in enumerate(in_deg):
            if not f:
                if ret!=-1:
                    return -1
                ret=i
        return ret

# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,2],[1,3],[1,2]]\n
# @lcpr case=end

#


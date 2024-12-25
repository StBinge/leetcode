#
# @lc app=leetcode.cn id=2285 lang=python3
# @lcpr version=30204
#
# [2285] 道路的最大总重要性
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree=[0]*n
        for a,b in roads:
            degree[a]+=1
            degree[b]+=1
        degree.sort()
        return sum(i*n for i,n in enumerate(degree,1))
# @lc code=end



#
# @lcpr case=start
# 5\n[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,3],[2,4],[1,3]]\n
# @lcpr case=end

#


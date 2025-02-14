#
# @lc app=leetcode.cn id=2492 lang=python3
# @lcpr version=30204
#
# [2492] 两个城市间路径的最小分数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        p=list(range(n+1))
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
        min_dist={}
        for x,y,d in roads:
            px,py=find(x),find(y)
            dd=min_dist.get(px,float('inf'))
            if px!=py:
                p[py]=px
                dd=min(dd,min_dist.get(py,float('inf')))
            min_dist[px]=min(dd,d)
        return min_dist[find(1)]
# @lc code=end
assert Solution().minScore(7,[[1,3,1484],[3,2,3876],[2,4,6823],[6,7,579],[5,6,4436],[4,5,8830]])==579
assert Solution().minScore(n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]])==2
assert Solution().minScore(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]])==5


#
# @lcpr case=start
# 4\n[[1,2,9],[2,3,6],[2,4,5],[1,4,7]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[1,2,2],[1,3,4],[3,4,7]]\n
# @lcpr case=end

#


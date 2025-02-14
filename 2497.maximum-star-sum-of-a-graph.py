#
# @lc app=leetcode.cn id=2497 lang=python3
# @lcpr version=30204
#
# [2497] 图中最大星和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adj=defaultdict(list)
        for x,y in edges:
            if vals[y]>0:
                adj[x].append(vals[y])
            if vals[x]>0:
                adj[y].append(vals[x])
        ret=float('-inf')
        for i,x in enumerate(vals):
            ret=max(ret,x+sum(heapq.nlargest(k,adj[i])))
        return ret
            
# @lc code=end
assert Solution().maxStarSum(vals = [-5], edges = [], k = 0)==-5
assert Solution().maxStarSum(vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2)==16


#
# @lcpr case=start
# [1,2,3,4,10,-10,-20]\n[[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [-5]\n[]\n0\n
# @lcpr case=end

#


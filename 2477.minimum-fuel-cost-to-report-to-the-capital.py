#
# @lc app=leetcode.cn id=2477 lang=python3
# @lcpr version=30204
#
# [2477] 到达首都的最少油耗
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0
        N=len(roads)+1
        adj=[[] for _ in range(N)]
        for x,y in roads:
            adj[x].append(y)
            adj[y].append(x)

        ret=0
        def dfs(cur,pre):
            nonlocal ret
            childs=0
            for nxt in adj[cur]:
                if nxt==pre:
                    continue
                cnt=dfs(nxt,cur)
                ret+=(cnt-1)//seats+1
                childs+=cnt
            return childs+1

        dfs(0,-1)
        return ret
# @lc code=end
assert Solution().minimumFuelCost(roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2)==7
assert Solution().minimumFuelCost(roads = [], seats = 1)==0
assert Solution().minimumFuelCost(roads = [[0,1],[0,2],[0,3]], seats = 5)==3


#
# @lcpr case=start
# [[0,1],[0,2],[0,3]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]\n2\n
# @lcpr case=end

# @lcpr case=start
# []\n1\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=2368 lang=python3
# @lcpr version=30204
#
# [2368] 受限条件下可到达节点的数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        vis = set()
        blocked = set(restricted)
        adj = [[] for _ in range(n)]
        for x, y in edges:
            if x not in blocked and y not in blocked:
                adj[x].append(y)
                adj[y].append(x)
        q = [0]
        while q:
            cur = q.pop()
            vis.add(cur)
            for nxt in adj[cur]:
                if nxt not in vis:
                    q.append(nxt)
        return len(vis)


# @lc code=end


#
# @lcpr case=start
# 7\n[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]\n[4,5]\n
# @lcpr case=end

# @lcpr case=start
# 7\n[[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]\n[4,2,1]\n
# @lcpr case=end

#

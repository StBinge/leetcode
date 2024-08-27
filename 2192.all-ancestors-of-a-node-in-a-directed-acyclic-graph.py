#
# @lc app=leetcode.cn id=2192 lang=python3
# @lcpr version=30204
#
# [2192] 有向无环图中一个节点的所有祖先
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj=defaultdict(list)
        for pa,ch in edges:
            adj[pa].append(ch)
        ret=[[] for _ in range(n)]
        vis=[-1]*n
        for i in range(n):
            q=[i]
            while q:
                pa=q.pop()
                for ch in adj[pa]:
                    if vis[ch]!=i:
                        ret[ch].append(i)
                        q.append(ch)
                        vis[ch]=i
        return ret
# @lc code=end
assert Solution().getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])==[[],[0],[0,1],[0,1,2],[0,1,2,3]]
assert Solution().getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])==[[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]


#
# @lcpr case=start
# 8\n[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]\n
# @lcpr case=end

#


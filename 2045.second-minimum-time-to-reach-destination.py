#
# @lc app=leetcode.cn id=2045 lang=python3
# @lcpr version=30204
#
# [2045] 到达目的地的第二短时间
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj=defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        inf=float('inf')
        dist=[[inf]*2 for i in range(n+1)]
        dist[1][0]=0
        q=deque([[0,1]])
        while dist[n][1]==inf:
            cost,node=q.popleft()
            for nxt in adj[node]:
                d=cost+1
                if d<dist[nxt][0]:
                    dist[nxt][0]=d
                    q.append([d,nxt])
                elif dist[nxt][0]<d<dist[nxt][1]:
                    dist[nxt][1]=d
                    q.append([d,nxt])
        
        ret=0
        c2=change*2
        for _ in range(dist[n][1]):
            if ret % c2 >=change:
                ret+=c2-ret%c2
            ret+=time
        return ret

# @lc code=end
assert Solution().secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2)==11
assert Solution().secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5)==13


#
# @lcpr case=start
# 5\n[[1,2],[1,3],[1,4],[3,4],[4,5]]\n3\n5\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,2]]\n3\n2\n
# @lcpr case=end

#


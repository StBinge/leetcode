#
# @lc app=leetcode.cn id=3372 lang=python3
# @lcpr version=30204
#
# [3372] 连接两棵树后最大目标节点数目 I
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        if k==0:
            return [1]*(len(edges1)+1)
        
        N=len(edges1)+1
        M=len(edges2)+1
        adj1=[[] for _ in range(N)]
        adj2=[[] for _ in range(M)]
        for x,y in edges1:
            adj1[x].append(y)
            adj1[y].append(x)
        for x,y in edges2:
            adj2[x].append(y)
            adj2[y].append(x)

        def get_path_cnt(adj,start,limit):
            N=len(adj)
            dist=[limit]*N
            dist[start]=0
            q=[[start,0,-1]]
            while q:
                cur,step,pre=q.pop()
                if step>dist[cur]:
                    continue
                step+=1
                for nxt in adj[cur]:
                    if nxt==pre or step>=dist[nxt]:
                        continue
                    dist[nxt]=step
                    q.append([nxt,step,cur])
            return sum(d<limit for d in dist)

        mx2=max(get_path_cnt(adj2,i,k) for i in range(M))
        ret=[]
        for i in range(N):
            ret.append(get_path_cnt(adj1,i,k+1)+mx2)
        return ret

# @lc code=end
assert Solution().maxTargetNodes([[0,1]],[[0,1]],0)==[1,1]
assert Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1)==[6,3,3,3,3]
assert Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2)==[9,7,9,8,8]


#
# @lcpr case=start
# [[0,1],[0,2],[2,3],[2,4]]\n[[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,2],[0,3],[0,4]]\n[[0,1],[1,2],[2,3]]\n1\n
# @lcpr case=end

#


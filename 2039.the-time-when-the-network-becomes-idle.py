#
# @lc app=leetcode.cn id=2039 lang=python3
# @lcpr version=30204
#
# [2039] 网络空闲的时刻
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        adj=defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        N=len(patience)
        dist=[float('inf')]*N
        dist[0]=0
        q=deque()
        q.append([0,0])
        while q:
            cost,cur=q.popleft()
            cost+=1
            for nxt in adj[cur]:
                if cost>=dist[nxt]:
                    continue
                q.append([cost,nxt])
                dist[nxt]=cost
        
        ret=0
        for i in range(1,N):
            get_recv=dist[i]*2
            last_send=(get_recv-1)//patience[i]*patience[i]
            ret=max(ret,last_send+2*dist[i]+1)
        return ret

# @lc code=end
assert Solution().networkBecomesIdle([[5,7],[15,18],[12,6],[5,1],[11,17],[3,9],[6,11],[14,7],[19,13],[13,3],[4,12],[9,15],[2,10],[18,4],[5,14],[17,5],[16,2],[7,1],[0,16],[10,19],[1,8]],[0,2,1,1,1,2,2,2,2,1,1,1,2,1,1,1,1,2,1,1])==67
assert Solution().networkBecomesIdle(edges = [[0,1],[1,2]], patience = [0,2,1])==8


#
# @lcpr case=start
# [[0,1],[1,2]]\n[0,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,2],[1,2]]\n[0,10,10]\n
# @lcpr case=end

#


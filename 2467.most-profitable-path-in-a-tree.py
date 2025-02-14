#
# @lc app=leetcode.cn id=2467 lang=python3
# @lcpr version=30204
#
# [2467] 树上最大得分和路径
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        N=len(edges)+1
        adj=[[] for _ in range(N)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        bob_path=[bob]
        bob_tick={}

        def find_bob_path(cur,pre):
            if bob_tick:
                return
            if cur==0:
                n=len(bob_path)
                for i in range(n):
                    bob_tick[bob_path[i]]=i
            for nxt in adj[cur]:
                if pre==nxt:
                    continue
                bob_path.append(nxt)
                find_bob_path(nxt,cur)
                bob_path.pop()
        
        find_bob_path(bob,-1)

        ret=float('-inf')
        def dfs(cur,pre,score,tick):
            btick=bob_tick.get(cur,10**6)
            if btick==tick:
                score+=amount[cur]//2
            elif tick<btick:
                score+=amount[cur]
            if len(adj[cur])==1 and adj[cur][0]==pre:
                nonlocal ret
                ret=max(ret,score)
                return
            for nxt in adj[cur]:
                if nxt==pre:
                    continue
                dfs(nxt,cur,score,tick+1)
        
        dfs(0,-1,0,0)
        return ret
# @lc code=end

assert Solution().mostProfitablePath(edges = [[0,1]], bob = 1, amount = [-7280,2350])==-7280
assert Solution().mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6])==6

#
# @lcpr case=start
# [[0,1],[1,2],[1,3],[3,4]]\n3\n[-2,4,2,-4,6]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1]]\n1\n[-7280,2350]\n
# @lcpr case=end

#


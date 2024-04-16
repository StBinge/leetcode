#
# @lc app=leetcode.cn id=1519 lang=python3
#
# [1519] 子树中标签相同的节点数
#
from sbw import *
# @lc code=start
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph=[[] for _ in range(n)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ret=[0]*n
        def travers(cur,par):
            cnt=[0]*26
            code=ord(labels[cur])-ord('a')
            cnt[code]+=1
            for nxt in graph[cur]:
                if nxt==par:
                    continue
                for i,c in enumerate(travers(nxt,cur)):
                    cnt[i]+=c
            ret[cur]=cnt[code]
            return cnt
        
        travers(0,-1)
        return ret
# @lc code=end
assert Solution().countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb")==[4,2,1,1]
assert Solution().countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd")==[2,1,1,1,1,1,1]

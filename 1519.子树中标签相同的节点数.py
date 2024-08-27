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

        counter=[[0]*26 for _ in range(n)]
        def dfs(cur_node,parent_node):
            code=ord(labels[cur_node])-ord('a')
            counter[cur_node][code]=1
            for nxt_node in graph[cur_node]:
                if nxt_node==parent_node:
                    continue
                dfs(nxt_node,cur_node)
                for j in range(26):
                    counter[cur_node][j]+=counter[nxt_node][j]
        dfs(0,-1)
        return [counter[i][ord(labels[i])-ord('a')] for i in range(n)]
# @lc code=end
assert Solution().countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb")==[4,2,1,1]
assert Solution().countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd")==[2,1,1,1,1,1,1]

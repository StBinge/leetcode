#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#
from typing import List
# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret=[]
        N=len(graph)
        def dfs(node,path:list):
            nonlocal N
            if node==N-1:
                ret.append(path.copy())
            for nxt in graph[node]:
                path.append(nxt)
                dfs(nxt,path)
                path.pop()
        dfs(0,[0])
        return ret
# @lc code=end
graph = [[1,2],[3],[3],[]]
print(Solution().allPathsSourceTarget(graph))
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(Solution().allPathsSourceTarget(graph))

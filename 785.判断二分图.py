#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nocolor,red,green=0,1,2
        colored=[nocolor]*len(graph)
        for i in range(len(graph)):
            if colored[i]>nocolor:
                continue
            queue=deque()
            queue.append(i)
            colored[i]=red
            while queue:
                cur=queue.popleft()
                nxt_color=green if colored[cur]==red else red
                for nei in graph[cur]:
                    if colored[nei]==nocolor:
                        colored[nei]=nxt_color
                        queue.append(nei)
                    elif colored[nei]!=nxt_color:
                        return False
        return True


# @lc code=end
assert Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]])==False
assert Solution().isBipartite([[1],[0,3],[3],[1,2]])

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
assert Solution().isBipartite(graph)==False

graph = [[1,3],[0,2],[1,3],[0,2]]
assert Solution().isBipartite(graph)

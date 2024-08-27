#
# @lc app=leetcode.cn id=1557 lang=python3
#
# [1557] 可以到达所有点的最少点数目
#
from sbw import *
# @lc code=start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        is_chlid=[False for _ in range(n)]
        for _,y in edges:
            is_chlid[y]=True
        return [i for i in range(n) if not is_chlid[i]]

        
# @lc code=end
assert Solution().findSmallestSetOfVertices(n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]])==[0,2,3]
assert Solution().findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]])==[0,3]

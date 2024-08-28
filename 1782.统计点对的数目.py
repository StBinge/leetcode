#
# @lc app=leetcode.cn id=1782 lang=python3
#
# [1782] 统计点对的数目
#
from sbw import *


# @lc code=start
class Solution:
    def countPairs(
        self, n: int, edges: List[List[int]], queries: List[int]
    ) -> List[int]:
        degree = [0] * n
        counter=defaultdict(int)
        for x, y in edges:
            x -= 1
            y -= 1
            if x>y:
                x,y=y,x
            degree[x] += 1
            degree[y] += 1
            counter[(x,y)]+=1
            
        # sorted_idx = sorted(range(n), key=degree.__getitem__)
        sorted_degree=sorted(degree)
        ret = []
        for i, q in enumerate(queries):
            left,right=0,n-1
            s=0
            while left<right:
                if sorted_degree[left]+sorted_degree[right]<=q:
                    left+=1
                else:
                    s+=right-left
                    right-=1

            for (x,y),cnt in counter.items():
                if degree[x]+degree[y]>q and degree[x]+degree[y]-cnt<=q:
                    s-=1
            ret.append(s)
        return ret


# @lc code=end
assert Solution().countPairs(6,[[5,2],[3,5],[4,5],[1,5],[1,4],[3,5],[2,6],[6,4],[5,6],[4,6],[6,2],[2,6],[5,4],[6,1],[6,1],[2,5],[1,3],[1,3],[4,5]],[6,9,2,1,2,3,6,6,6,5,9,7,0,4,5,9,1,18,8,9])==[15,13,15,15,15,15,15,15,15,15,13,15,15,15,15,13,15,0,14,13]
assert Solution().countPairs(n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5])==[10,10,9,8,6]
assert Solution().countPairs(
    n=4, edges=[[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], queries=[2, 3]
) == [6, 5]

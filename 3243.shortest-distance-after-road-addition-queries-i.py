#
# @lc app=leetcode.cn id=3243 lang=python3
# @lcpr version=30204
#
# [3243] 新增道路查询后的最短距离 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:        
        f=list(range(n))
        left=[[] for _ in range(n)]
        ret=[]
        for x,y in queries:
            left[y].append(x)
            if f[y]>f[x]+1:
                f[y]=f[x]+1
                for i in range(y+1,n):
                    f[i]=min(f[i-1]+1,min([f[j] for j in left[i]],default=float('inf'))+1)
            ret.append(f[-1])
        return ret
        
# @lc code=end
assert Solution().shortestDistanceAfterQueries(10,[[3,8],[3,6],[1,3],[1,7],[0,8],[1,8]])==[5,5,4,4,2,2]
assert Solution().shortestDistanceAfterQueries(7,[[4,6],[0,3]])==[5,3]
assert Solution().shortestDistanceAfterQueries( n = 4, queries = [[0, 3], [0, 2]])==[1,1]
assert Solution().shortestDistanceAfterQueries( n = 5, queries = [[2, 4], [0, 2], [0, 4]])==[3,2,1]


#
# @lcpr case=start
# 5\n[[2, 4], [0, 2], [0, 4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0, 3], [0, 2]]\n
# @lcpr case=end

#


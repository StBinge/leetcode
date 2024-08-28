#
# @lc app=leetcode.cn id=1971 lang=python3
# @lcpr version=30204
#
# [1971] 寻找图中是否存在路径
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        p=list(range(n))

        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
        
        def connect(x,y):
            x,y=find(x),find(y)
            p[x]=y
        
        for x,y in edges:
            connect(x,y)
        
        return find(source)==find(destination)
# @lc code=end
assert Solution().validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2)


#
# @lcpr case=start
# 3\n[[0,1],[1,2],[2,0]]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[0,1],[0,2],[3,5],[5,4],[4,3]]\n0\n5\n
# @lcpr case=end

#


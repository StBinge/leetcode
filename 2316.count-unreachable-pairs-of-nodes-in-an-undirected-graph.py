#
# @lc app=leetcode.cn id=2316 lang=python3
# @lcpr version=30204
#
# [2316] 统计无向图中无法互相到达点对数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        p=list(range(n))
        size=[1]*n
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            if size[px]>size[py]:
                p[py]=px
                size[px]+=size[py]
            else:
                p[px]=py
                size[py]+=size[px]
        
        for x,y in edges:
            union(x,y)
        
        ret=0
        s=0
        for i,pa in enumerate(p):
            if i==pa:
                ret+=s*size[i]
                s+=size[i]
        return ret
        

# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1],[0,2],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# 7\n[[0,2],[0,5],[2,4],[1,6],[5,4]]\n
# @lcpr case=end

#


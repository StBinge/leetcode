#
# @lc app=leetcode.cn id=2685 lang=python3
# @lcpr version=30204
#
# [2685] 统计完全连通分量的数量
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        pa=list(range(n))
        edge_cnt=[0]*n
        node_cnt=[1]*n

        def find(x):
            if x!=pa[x]:
                pa[x]=find(pa[x])
            return pa[x]

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                edge_cnt[px]+=1
                return
            if node_cnt[px]>node_cnt[py]:
                px,py=py,px
            pa[px]=py
            node_cnt[py]+=node_cnt[px]
            edge_cnt[py]+=edge_cnt[px]+1
        
        for x,y in edges:
            union(x,y)
        
        ret=0
        for i,p in enumerate(pa):
            if i==p:
                nodes=node_cnt[i]
                target=(nodes-1)*nodes//2
                if target==edge_cnt[i]:
                    ret+=1
        return ret
        
# @lc code=end



#
# @lcpr case=start
# 6\n[[0,1],[0,2],[1,2],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[0,1],[0,2],[1,2],[3,4],[3,5]]\n
# @lcpr case=end

#


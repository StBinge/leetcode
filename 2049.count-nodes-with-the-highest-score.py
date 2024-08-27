#
# @lc app=leetcode.cn id=2049 lang=python3
# @lcpr version=30204
#
# [2049] 统计最高分的节点数目
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N=len(parents)
        out_deg=[0]*N
        childs=[[] for _ in range(N)]
        for idx in range(1,N):
            p=parents[idx]
            out_deg[p]+=1
            childs[p].append(idx)
        leaves=[i for i,deg in enumerate(out_deg) if deg==0]
        out_deg[0]=3
        childs_cnt=[1]*N
        while leaves:
            node=leaves.pop()
            p=parents[node]
            childs_cnt[p]+=childs_cnt[node]
            out_deg[p]-=1
            if out_deg[p]==0:
                leaves.append(p)
        
        Mx=ret=0
        tot=childs_cnt[0]
        for i in range(N):
            val=1
            for child in childs[i]:
                val*= childs_cnt[child]
            other=tot-childs_cnt[i]
            if other:
                val*=other
            if val>Mx:
                Mx=val
                ret=1
            elif Mx==val:
                ret+=1
        return ret

# @lc code=end
assert Solution().countHighestScoreNodes([-1,2,0])==2
assert Solution().countHighestScoreNodes([-1,2,0,2,0])==3


#
# @lcpr case=start
# [-1,2,0,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [-1,2,0]\n
# @lcpr case=end

#


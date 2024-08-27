#
# @lc app=leetcode.cn id=1659 lang=python3
#
# [1659] 最大化网格幸福感
#
from sbw import *
# @lc code=start
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:

        T=3**n
        inner_score=[0]*T
        inter_score=[[0]*T for _ in range(T)]
        adj_score=[
            [0,0,0],
            [0,-60,-10],
            [0,-10,40]
        ]
        inv_cnt=[0]*T
        ext_cnt=[0]*T
        def init_inner_score():
            for i in range(T):
                pre_bit=0
                mask=i
                v=0
                while mask:
                    cur_bit=mask%3
                    if cur_bit==1:
                        v+=120
                        inv_cnt[i]+=1
                    elif cur_bit==2:
                        ext_cnt[i]+=1
                        v+=40
                    v+=adj_score[cur_bit][pre_bit]
                    pre_bit=cur_bit
                    mask//=3
                inner_score[i]=v
        
        def init_inter_score():
            for i in range(T):
                for j in range(i,T):
                    v=0
                    mi,mj=i,j
                    while mi or mj:
                        b1=mi%3
                        b2=mj%3
                        v+=adj_score[b1][b2]
                        mi//=3
                        mj//=3
                    inter_score[i][j]=v
                    inter_score[j][i]=v

        init_inner_score()
        init_inter_score()

        @cache
        def dfs(rid,intro,extro,premask):
            if rid==m or intro+extro==0:
                return 0
            ret=0
            for i in range(T):
                if inv_cnt[i]>intro or ext_cnt[i]>extro:
                    continue
                ret=max(
                    ret,
                    dfs(rid+1,intro-inv_cnt[i],extro-ext_cnt[i],i)+inner_score[i]+inter_score[i][premask])
                # print(ret)
            return ret

        ret= dfs(0,introvertsCount,extrovertsCount,0)  
        return ret
# @lc code=end
assert Solution().getMaxGridHappiness(5,4,6,3)==920
assert Solution().getMaxGridHappiness(m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1)==260
assert Solution().getMaxGridHappiness(m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2)==240

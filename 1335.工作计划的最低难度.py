#
# @lc app=leetcode.cn id=1335 lang=python3
#
# [1335] 工作计划的最低难度
#
from sbw import *
# @lc code=start
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        L=len(jobDifficulty)
        if L<d:
            return -1
        f=[[float('inf')]*L for _ in range(d)]
        dif=0
        for i in range(L):
            dif=max(dif,jobDifficulty[i])
            f[0][i]=dif
        for i in range(1,d):
            st=[]
            for j in range(i,L):
                mn=f[i-1][j-1]
                while st and jobDifficulty[st[-1][0]]<=jobDifficulty[j]:
                    mn=min(mn,st.pop()[1])
                f[i][j]=mn+jobDifficulty[j]
                if st:
                    f[i][j]=min(f[i][j],f[i][st[-1][0]])
                st.append([j,mn])
        return f[-1][-1]

# @lc code=end
assert Solution().minDifficulty(jobDifficulty = [9,9,9],d=4)==-1
assert Solution().minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2)==7

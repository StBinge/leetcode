#
# @lc app=leetcode.cn id=1718 lang=python3
#
# [1718] 构建字典序最大的可行序列
#
from sbw import *
# @lc code=start
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        N=n*2-1
        ret=[0]*N
        used=[False]*(n+1)
        # idx=0
        # for i in range(n,1,-2):
        #     ret[idx]=ret[idx+i]=i
        #     idx+=1
        #     used[i]=True
        def dfs(idx):
            while idx<N and ret[idx]:
                idx+=1
            if idx==N:
                return True
            for i in range(n,1,-1):
                if used[i] or idx+i>=N or ret[idx+i]:
                    continue
                ret[idx]=ret[idx+i]=i
                used[i]=True
                if dfs(idx+1):
                    return True
                ret[idx]=ret[idx+i]=0
                used[i]=False
            if not used[1]:
                ret[idx]=1
                used[1]=True
                if dfs(idx+1):
                    return True
                ret[idx]=0
                used[1]=False

            return False
        dfs(0)
        return ret
# @lc code=end
assert Solution().constructDistancedSequence(10)==[10,8,6,9,3,1,7,3,6,8,10,5,9,7,4,2,5,2,4]
assert Solution().constructDistancedSequence(5)==[5,3,1,4,3,5,2,4,2]
assert Solution().constructDistancedSequence(2)==[2,1,2]
assert Solution().constructDistancedSequence(3)==[3,1,2,3,2]

#
# @lc app=leetcode.cn id=1928 lang=python3
# @lcpr version=30204
#
# [1928] 规定时间内到达终点的最小花费
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        N=len(passingFees)
        f=[[float('inf')]*N for _ in range(maxTime+1)]
        f[0][0]=passingFees[0]

        for t in range(1,maxTime+1):
            for i,j,cost in edges:
                if cost>t:
                    continue
                f[t][i]=min(f[t][i],f[t-cost][j]+passingFees[i])
                f[t][j]=min(f[t][j],f[t-cost][i]+passingFees[j])
        
        ret=min(f[t][-1] for t in range(1,maxTime+1))
        return -1 if math.isinf(ret) else ret
# @lc code=end
assert Solution().minCost(maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3])==48
assert Solution().minCost(maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3])==-1
assert Solution().minCost(maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3])==11


#
# @lcpr case=start
# 30\n[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]\n[5,1,2,20,20,3]\n
# @lcpr case=end

# @lcpr case=start
# 29\n[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]\n[5,1,2,20,20,3]\n
# @lcpr case=end

# @lcpr case=start
# 25\n[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]\n[5,1,2,20,20,3]\n
# @lcpr case=end

#


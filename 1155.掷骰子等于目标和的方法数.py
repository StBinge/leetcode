#
# @lc app=leetcode.cn id=1155 lang=python3
#
# [1155] 掷骰子等于目标和的方法数
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        f=[0]*(target+1)
        f[0]=1
        for i in range(n):
            for j in range(target,-1,-1):
                f[j]=0
                for x in range(1,min(k,j)+1):
                    f[j]+=f[j-x]
                f[j]%=(10**9+7)
        return f[-1]
# @lc code=end
assert Solution().numRollsToTarget(n = 30, k = 30, target = 500)==222616187
assert Solution().numRollsToTarget(n = 2, k = 6, target = 7)==6
assert Solution().numRollsToTarget(n = 1, k = 6, target = 3)==1

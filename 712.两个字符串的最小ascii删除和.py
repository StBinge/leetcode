#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小ASCII删除和
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        L1,L2=len(s1),len(s2)
        # dp=[[float('inf')]*(L2+1) for _ in range(L1+1)]
        # dp[0][0]=0
        # for i in range(L1):
        #     dp[i+1][0]=dp[i][0]+ord(s1[i])
        # for j in range(L2):
        #     dp[0][j+1]=dp[0][j]+ord(s2[j])
        dp=[0]*(L2+1)
        # dp[0]=0
        for i in range(L2):
            dp[i+1]=dp[i]+ord(s2[i])

        for i in range(1,L1+1):
            pre=dp[0]
            dp[0]+=ord(s1[i-1])
            for j in range(1,L2+1):
                temp=dp[j]
                if s1[i-1]==s2[j-1]:
                    dp[j]=pre
                else:
                    dp[j]=min(dp[j]+ord(s1[i-1]),dp[j-1]+ord(s2[j-1]))
                pre=temp
        return dp[-1]
# @lc code=end
s1 = "sea"
s2 = "eat"
# assert Solution().minimumDeleteSum(s1,s2)==231
s1 = "delete"
s2 = "leet"
assert Solution().minimumDeleteSum(s1,s2)==403


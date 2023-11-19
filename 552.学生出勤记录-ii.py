#
# @lc app=leetcode.cn id=552 lang=python3
#
# [552] 学生出勤记录 II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD=10**9+7
        dp=[[0]*3 for _ in range(2)]
        dp[0][0]=1
        for i in range(1,n+1):
            dp_new=[[0,0,0],[0,0,0]]
            # end with P
            # same A
            # clear L
            for j in range(2):
                for k in range(3):
                    dp_new[j][0]=(dp_new[j][0]+dp[j][k])%MOD
            
            # end with A
            # add A
            # clear L
            for k in range(3):
                dp_new[1][0]=(dp_new[1][0]+dp[0][k])%MOD
            
            # end with L
            # keep A
            # resitric L<2
            for j in range(2):
                for k in range(1,3):
                    dp_new[j][k]=(dp_new[j][k]+dp[j][k-1])%MOD
            dp=dp_new
        return (sum(dp[0])+sum(dp[1]))%MOD
        

# @lc code=end

assert Solution().checkRecord(10101)==183236316
assert Solution().checkRecord(2)==8
assert Solution().checkRecord(1)==3
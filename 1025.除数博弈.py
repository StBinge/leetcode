#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#

# @lc code=start
class Solution:
    def divisorGame(self, n: int) -> bool:
        f=[False]*(n+2)
        f[1]=False
        f[2]=True
        # f[3]=False
        for i in range(3,n+1):
            for j in range(1,i):
                if i %j==0 and not f[i-j]:
                    f[i]=True
                    break
        return f[n]
# @lc code=end
assert Solution().divisorGame(2)
assert Solution().divisorGame(26)
assert Solution().divisorGame(3)==False
assert Solution().divisorGame(11)==False

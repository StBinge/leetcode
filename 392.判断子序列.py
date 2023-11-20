#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls,lt=len(s),len(t)
        dp=[[0]*26 for _ in range(lt)]
        dp.append([lt]*26)
        orda=ord('a')
        for i in range(lt-1,-1,-1):
            for j in range(26):
                dp[i][j]=dp[i+1][j]
            dp[i][ord(t[i])-orda]=i
        
        start=0
        for i in range(ls):
            if dp[start][ord(s[i])-orda]==lt:
                return False
            start=dp[start][ord(s[i])-orda]+1
        return True

# @lc code=end
assert Solution().isSubsequence('b','c')==False
assert Solution().isSubsequence('aaaaaa','bbaaaa')==False
assert Solution().isSubsequence('abc','ahbgdc')
assert Solution().isSubsequence('axc','ahbgdc')==False
assert Solution().isSubsequence('aaaa','bbaaaa')==True

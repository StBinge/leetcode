#
# @lc app=leetcode.cn id=467 lang=python3
#
# [467] 环绕字符串中唯一的子字符串
#

# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp={}
        k=1
        dp[s[0]]=1
        for i in range(1,len(s)):
            if (ord(s[i])-ord(s[i-1])) % 26==1:
                k+=1
            else:
                k=1
            cnt=dp.get(s[i],0)
            dp[s[i]]=max(k,cnt)
        return sum(dp.values())
# @lc code=end


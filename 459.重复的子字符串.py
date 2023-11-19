#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#
from typing import List
# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        nxt=[0]*len(s)
        k=0
        for i in range(1,len(s)):
            while k>0 and s[k]!=s[i]:
                k=nxt[k-1]
            if s[k]==s[i]:
                k+=1
            nxt[i]=k
        
        return nxt[-1]!=0 and len(s) % (len(s)-nxt[-1])==0
        

# @lc code=end
assert Solution().repeatedSubstringPattern('aaaa')==True
assert Solution().repeatedSubstringPattern('abac')==False
assert Solution().repeatedSubstringPattern('aba')==False
assert Solution().repeatedSubstringPattern('abab')
assert Solution().repeatedSubstringPattern('abcabcabcabc')

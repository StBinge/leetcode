#
# @lc app=leetcode.cn id=1397 lang=python3
#
# [1397] 找到所有好字符串
#
from sbw import *
# @lc code=start
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        idx=0
        while idx<n and s1[idx]==s2[idx]:
            idx+=1
        if s1[:idx].find(evil)>=0:
            return 0
        
        m=len(evil)
        fail=[0]*m
        j=0
        for i in range(1,m):
            j=fail[i-1]
            while j>0 and evil[j]!=evil[i]:
                j=fail[j-1]
            if evil[j]==evil[i]:
                fail[i]=j+1
        @cache
        def trans(state,ch):
            # ch=ord(ch)-ord('a')
            while state>0 and evil[state]!=ch:
                state=fail[state-1]
            return state+int(evil[state]==ch)

        @cache
        def dp(pos:int,bound:int,state):
            if state==m:
                return 0
            if pos==n:
                return 1
            lower=s1[pos] if bound & 1 else 'a'
            upper=s2[pos] if bound & 0b10 else 'z'
            ret=0
            for cod in range(ord(lower),ord(upper)+1):
                ch=chr(cod)
                nxt_state=trans(state,ch)
                nxt_bound=0
                if bound & 1 and ch==lower:
                    nxt_bound|=1
                if bound & 0b10 and ch==upper:
                    nxt_bound|=0b10
                ret+=dp(pos+1,nxt_bound,nxt_state)
            return ret % (10**9+7)
        return dp(0,3,0)

# @lc code=end
assert Solution().findGoodStrings(n = 2, s1 = "aa", s2 = "da", evil = "b")==51
assert Solution().findGoodStrings(n = 2, s1 = "aa", s2 = "da", evil = "b")==51

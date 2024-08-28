#
# @lc app=leetcode.cn id=1737 lang=python3
#
# [1737] 满足三条件之一需改变的最少字符数
#
from sbw import *
# @lc code=start
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        def count(s:str):
            cnt=[0]*26
            for ch in s:
                cnt[ord(ch)-ord('a')]+=1
            return cnt

        cnt1=count(a)
        cnt2=count(b)
        presum1=list(accumulate(cnt1,lambda x,y:x+y,initial=0))
        presum2=list(accumulate(cnt2,lambda x,y:x+y,initial=0))
        
        tot=presum1[-1]+presum2[-1]
        ret=tot-cnt1[0]-cnt2[0]
        for i in range(1,26):
            # change2small=cnt1[-1]-cnt1[i]
            # change2big=cnt2[i]
            ret=min(ret,presum1[-1]-presum1[i]+presum2[i],presum2[-1]-presum2[i]+presum1[i],tot-cnt1[i]-cnt2[i])
        return ret


# @lc code=end
assert Solution().minCharacters('e','e')==0
assert Solution().minCharacters(a = "dabadd", b = "cda")==3
assert Solution().minCharacters(a = "aba", b = "caa")==2

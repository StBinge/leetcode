#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L1=len(s1)
        L=len(s2)
        if L1>L:
            return False
        orda=ord('a')
        cnt=[0]*26
        for i in range(L1):
            c1=ord(s1[i])-orda
            # c2=ord(s2[i])-orda
            cnt[c1]+=1
            # cnt[c2]-=1
        
        left=0
        for i in range(L):
            c2=ord(s2[i])-orda
            cnt[c2]-=1
            while cnt[c2]<0:
                c1=ord(s2[left])-orda
                cnt[c1]+=1
                left+=1
            if i-left+1==L1:
                return True
        return False
            


            
                    
    
# @lc code=end

assert Solution().checkInclusion('adc','dcda')
assert Solution().checkInclusion('ab','eidbaooo')
assert Solution().checkInclusion('ab','eidboaooo')==False
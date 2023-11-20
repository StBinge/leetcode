#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from typing import List
# @lc code=start

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

   
        lp=len(p)
        ls=len(s)
        if lp>ls:
            return []
        window=[0]*26
        orda=ord('a')
        for i in range(lp):
            window[ord(s[i])-orda]+=1
            window[ord(p[i])-orda]-=1
        
        diff=[w!=0 for w in window].count(True)
        ret=[]
        if diff==0:
            ret.append(0)
        
        for i in range(ls-lp):
            ords=ord(s[i])-orda
            window[ords]-=1
            if window[ords]==-1:
                diff+=1
            elif window[ords]==0:
                diff-=1
            ords=ord(s[i+lp])-orda
            window[ords]+=1
            if window[ords]==0:
                diff-=1
            elif window[ords]==1:
                diff+=1
            if diff==0:
                ret.append(i+1)
        return ret

# @lc code=end

print(Solution().findAnagrams('cbaebabacd','abc'))
print(Solution().findAnagrams('abab','ab'))
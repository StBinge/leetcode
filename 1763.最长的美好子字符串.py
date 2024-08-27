#
# @lc app=leetcode.cn id=1763 lang=python3
#
# [1763] 最长的美好子字符串
#
from sbw import *


# @lc code=start
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        N = len(s)
        max_len = 0
        pos = 0
        ordA = ord("A")
        orda = ord("a")
        def check(limit):
            lower_cnt=[0]*26
            upper_cnt=[0]*26
            tot=valid=0
            l=0
            for r in range(N):
                code=ord(s[r])
                if code>90:
                    idx=code-orda
                    lower_cnt[idx]+=1
                    if lower_cnt[idx]==1 and upper_cnt[idx]:
                        valid+=1
                else:
                    idx=code-ordA
                    upper_cnt[idx]+=1
                    if upper_cnt[idx]==1 and lower_cnt[idx]:
                        valid+=1
                if lower_cnt[idx]+upper_cnt[idx]==1:
                    tot+=1
                
                while tot>limit:
                    code=ord(s[l])
                    if code>90:
                        idx=code-orda
                        lower_cnt[idx]-=1
                        if not lower_cnt[idx] and upper_cnt[idx]:
                            valid-=1
                    else:
                        idx=code-ordA
                        upper_cnt[idx]-=1
                        if not upper_cnt[idx] and lower_cnt[idx]:
                            valid-=1

                    if lower_cnt[idx]==upper_cnt[idx]==0:
                        tot-=1
                    l+=1
                if valid==limit:
                    found=True
                    nonlocal max_len,pos
                    length=r-l+1
                    if length>max_len:
                        max_len=length
                        pos=l
            
        left,right=1,len(set(s.lower()))
        for i in range(left,right+1):
            check(i)
        return s[pos:pos+max_len]

# @lc code=end
assert Solution().longestNiceSubstring("BebjJE") == "BebjJE"
assert Solution().longestNiceSubstring("YazaAay") == "aAa"
assert Solution().longestNiceSubstring("dDzeE") == "dD"
assert Solution().longestNiceSubstring("c") == ""
assert Solution().longestNiceSubstring("bB") == "bB"

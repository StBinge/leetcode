#
# @lc app=leetcode.cn id=1156 lang=python3
#
# [1156] 单字符重复子串的最大长度
#
from sbw import *
# @lc code=start
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counter=Counter(text)
        i=0
        L=len(text)
        ret=0
        char=''
        pre=None
        ppre=None
        cur=None
        while i<L:
            j=i
            while j<L and text[j]==text[i]:
                i+=1
            cur=[text[j],j-i]
            
        return ret
# @lc code=end
assert Solution().maxRepOpt1('abcdef')==1
assert Solution().maxRepOpt1('aaaaa')==5
assert Solution().maxRepOpt1('aaabbaaa')==4
assert Solution().maxRepOpt1('aaabaaa')==6
assert Solution().maxRepOpt1('ababa')==3

#
# @lc app=leetcode.cn id=1147 lang=python3
#
# [1147] 段式回文
#
from sbw import *
# @lc code=start
class Solution:
    def longestDecomposition(self, text: str) -> int:
        L=len(text)
        l,r=0,L-1
        ret=0
        while l<=r:
            length=1
            while l+length < r-length+2 and text[l:l+length]!=text[r+1-length:r+1]:
                length+=1
            if l+length<r-length+2:
                ret+=2
            else:
                ret+=1
            l=l+length
            r=r-length
        return ret

# @lc code=end
ret= Solution().longestDecomposition('aaa')
assert ret==3

ret= Solution().longestDecomposition('antaprezatepzapreanta')
assert ret==11

ret= Solution().longestDecomposition('merchant')
assert ret==1

ret= Solution().longestDecomposition('ghiabcdefhelloadamhelloabcdefghi')
assert ret==7
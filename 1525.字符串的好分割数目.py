#
# @lc app=leetcode.cn id=1525 lang=python3
#
# [1525] 字符串的好分割数目
#
from sbw import *
# @lc code=start
class Solution:
    def numSplits(self, s: str) -> int:
        N=len(s)
        left=[0]*(N+1)
        vis=0
        orda=ord('a')
        for i,c in enumerate(s,1):
            mask=1<<(ord(c)-orda)
            if vis & mask:
                left[i]=left[i-1]
            else:
                left[i]=left[i-1]+1
                vis |= mask
        right=[0]*(N+1)
        vis=0
        for i in range(N-1,-1,-1):
            mask=1<<(ord(s[i])-orda)
            if vis & mask:
                right[i]=right[i+1]
            else:
                right[i]=right[i+1]+1
                vis |= mask
        
        return sum(left[i]==right[i] for i in range(1,N))

            

# @lc code=end
assert Solution().numSplits("acbadbaada")==2
assert Solution().numSplits("aaaaa")==4
assert Solution().numSplits("abcd")==1
assert Solution().numSplits("abcd")==1

#
# @lc app=leetcode.cn id=1297 lang=python3
#
# [1297] 子串的最大出现次数
#
from sbw import *
# @lc code=start
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ret=0
        orda=ord('a')
        # for sz in range(minSize,maxSize+1):
        sz=minSize
        counter=defaultdict(int)
        chars=[0]*26
        letters=0
        code=0
        for i in range(sz):
            idx=ord(s[i])-orda
            chars[idx]+=1
            if chars[idx]==1:
                letters+=1
            code=code*26+idx
        if letters<=maxLetters:
            counter[code]+=1
        high=26**(sz-1)
        for i in range(sz,len(s)):
            idx=ord(s[i-sz])-orda
            chars[idx]-=1
            if chars[idx]==0:
                letters-=1
            code-=high*idx

            idx=ord(s[i])-orda
            chars[idx]+=1
            if chars[idx]==1:
                letters+=1
            code=code*26+idx
            if letters<=maxLetters:
                counter[code]+=1
        if counter:
            ret=max(counter.values())
        return ret
# @lc code=end
assert Solution().maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3)==0
assert Solution().maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3)==2
assert Solution().maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4)==2

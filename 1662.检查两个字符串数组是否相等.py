#
# @lc app=leetcode.cn id=1662 lang=python3
#
# [1662] 检查两个字符串数组是否相等
#
from sbw import *
# @lc code=start
from itertools import chain
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        N1=len(word1)
        N2=len(word2)
        i,j,ii,jj=0,0,0,0
        while i<N1 and j<N2:
            if word1[i][ii]!=word2[j][jj]:
                return False
            ii+=1
            if ii==len(word1[i]):
                ii=0
                i+=1
            jj+=1
            if jj==len(word2[j]):
                jj=0
                j+=1
        return i==N1 and j==N2        
# @lc code=end
assert not Solution().arrayStringsAreEqual(["abc","d","defg"],["abcddef"])
assert not Solution().arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"])
assert Solution().arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"])

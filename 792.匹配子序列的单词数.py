#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#
from typing import List
# @lc code=start
import bisect
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos={}
        for i,word in enumerate(words):
            pos.setdefault(word[0],[]).append([i,0])
        ret=0
        for c in s:
            queue=pos.get(c,[])
            pos[c]=[]
            for i,j in queue:
                j+=1
                if j==len(words[i]):
                    ret+=1
                    continue
                pos.setdefault(words[i][j],[]).append([i,j])
        return ret
# @lc code=end
s = "abcde"
words = ["a","bb","acd","ace"]
assert Solution().numMatchingSubseq(s,words)==3
s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
assert Solution().numMatchingSubseq(s,words)==2

#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#
from sbw import *
# @lc code=start
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        memo=[]
        orda=ord('a')
        chars=[0]*26
        for c in letters:
            chars[ord(c)-orda]+=1
        for word in words:
            cnt=[0]*26
            s=0
            for c in word:
                o=ord(c)-orda
                cnt[o]+=1
                s+=score[o]
            if all(c1<=c2 for c1,c2 in zip(cnt,chars)):
                memo.append([cnt,s])
        L=len(memo)
        ret=0
        for mask in range(1,1<<L):
            cnt=[0]*26
            ss=0
            for j in range(L):
                if mask & 1<<j:
                    w,s=memo[j]
                    for i in range(26):
                        cnt[i]+=w[i]
                    ss+=s
            if all(c1<=c2 for c1,c2 in zip(cnt,chars)):
                ret=max(ret,ss)
        return ret
# @lc code=end
assert Solution().maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0])==0
assert Solution().maxScoreWords(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10])==27
assert Solution().maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])==23

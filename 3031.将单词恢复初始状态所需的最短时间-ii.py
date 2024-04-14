#
# @lc app=leetcode.cn id=3031 lang=python3
#
# [3031] 将单词恢复初始状态所需的最短时间 II
#

# @lc code=start
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        L=len(word)
        next=[0]*L
        j=0
        for i in range(1,L):
            while j>0 and word[j]!=word[i]:
                j=next[j-1]
            if word[j]==word[i]:
                j+=1
                next[i]=j
        ret=next[-1]
        while ret and (L-ret)%k!=0:
            ret=next[ret-1]
        return (L-ret-1)//k+1 
    
# @lc code=end
assert Solution().minimumTimeToInitialState(word = "abacaba", k = 3)==2
assert Solution().minimumTimeToInitialState(word = "abacaba", k = 4)==1
assert Solution().minimumTimeToInitialState(word = "abcbabcd", k = 2)==4

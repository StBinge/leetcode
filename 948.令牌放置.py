#
# @lc app=leetcode.cn id=948 lang=python3
#
# [948] 令牌放置
#
from sbw import *
# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens or power<tokens[0]:
            return 0
        power-=tokens[0]
        score=1
        ret=1
        l,r=1,len(tokens)-1
        while l<r:
            while l<=r and power>=tokens[l]:
                score+=1
                power-=tokens[l]
                l+=1
            ret=max(ret,score)
            if l<=r and score>0:
                score-=1
                power+=tokens[r]
                r-=1
            else:
                break
        return ret
# @lc code=end
tokens=[48,87,26]
power=81
assert Solution().bagOfTokensScore(tokens,power)==2

tokens = [100,200,300,400]
power = 200
assert Solution().bagOfTokensScore(tokens,power)==2


tokens = [100,200]
power = 150
assert Solution().bagOfTokensScore(tokens,power)==1

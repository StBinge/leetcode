#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#
from sbw import *
# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt=Counter(text)
        return min(cnt['a'],cnt['b'],cnt['l']//2,cnt['o']//2,cnt['n'])
# @lc code=end
assert Solution().maxNumberOfBalloons('loonbalxballpoon')==2

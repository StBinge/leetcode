#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#
from sbw import *
# @lc code=start
# from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter=Counter(deck)
        n=len(deck)
        for v in counter.values():
            n=gcd(n,v)
        return n>=2       
# @lc code=end
assert Solution().hasGroupsSizeX([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3])==False
assert Solution().hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2])
assert Solution().hasGroupsSizeX([1,1,2,2,2,2])
assert Solution().hasGroupsSizeX([1,1])
assert Solution().hasGroupsSizeX([1])==False

deck = [1,1,1,2,2,2,3,3]
assert Solution().hasGroupsSizeX(deck)==False

deck = [1,2,3,4,4,3,2,1]
assert Solution().hasGroupsSizeX(deck)

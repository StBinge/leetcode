#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#
from sbw import *
# @lc code=start
import itertools
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(x+y for x,y in itertools.zip_longest(word1,word2,fillvalue=''))
# @lc code=end
assert Solution().mergeAlternately(word1 = "abc", word2 = "pqr")=="apbqcr"

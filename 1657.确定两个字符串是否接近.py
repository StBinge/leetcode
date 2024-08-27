#
# @lc app=leetcode.cn id=1657 lang=python3
#
# [1657] 确定两个字符串是否接近
#
from sbw import *


# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        N1, N2 = len(word1), len(word2)
        if N1 != N2:
            return False
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        if counter1.keys()!=counter2.keys():
            return False
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
        return True


# @lc code=end
assert Solution().closeStrings("uau","ssx")==False
assert Solution().closeStrings(word1="cabbba", word2="abbccc")
assert Solution().closeStrings(word1="cabbba", word2="abbccc")
assert Solution().closeStrings(word1="a", word2="aa") == False
assert Solution().closeStrings(word1="abc", word2="bca")

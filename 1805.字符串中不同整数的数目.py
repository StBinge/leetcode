#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#
from sbw import *


# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ret = set()
        l = 0
        for i, c in enumerate(word):
            if not c.isnumeric():
                if l != i:
                    ret.add(int(word[l:i]))
                l = i + 1
        if l != len(word):
            ret.add(int(word[l:]))
        return len(ret)


# @lc code=end
assert Solution().numDifferentIntegers("a1b01c001") == 1
assert Solution().numDifferentIntegers("leet1234code234") == 2
assert Solution().numDifferentIntegers("a123bc34d8ef34") == 3

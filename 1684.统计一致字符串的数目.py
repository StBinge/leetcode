#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#
from sbw import *
# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask=0
        for c in allowed:
            mask |= 1<<(ord(c)-ord('a'))
        ret=0
        for w in words:
            m=0
            for c in w:
                m |= 1<<(ord(c)-ord('a'))
            ret+=m|mask == mask
        return ret
# @lc code=end


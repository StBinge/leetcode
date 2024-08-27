#
# @lc app=leetcode.cn id=1880 lang=python3
#
# [1880] 检查某单词是否等于两单词之和
#
from sbw import *
# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(s:str):
            ret=0
            for c in s:
                code=ord(c)-ord('a')
                ret=ret*10+code
            return ret
        return convert(firstWord)+convert(secondWord)==convert(targetWord)
# @lc code=end


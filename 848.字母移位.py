#
# @lc app=leetcode.cn id=848 lang=python3
#
# [848] 字母移位
#
from typing import List
# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        S=sum(shifts)
        ret=['']*len(s)
        ord_a=ord('a')
        for i,c in enumerate(s):            
            ret[i]=chr((ord(c)+S-ord_a)%26+ord_a)
            S-=shifts[i]
        return ''.join(ret)
# @lc code=end
s = "aaa"
shifts = [1,2,3]
assert Solution().shiftingLetters(s,shifts)=='gfd'

s = "abc"
shifts = [3,5,9]
assert Solution().shiftingLetters(s,shifts)=='rpl'
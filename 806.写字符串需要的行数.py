#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#
from typing import List
# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total=0
        rows=1
        for c in s:
            nxt=widths[ord(c)-ord('a')]
            if total+nxt>100:
                rows+=1
                total=0
            total+=nxt
        return [rows,total]
# @lc code=end
widths=[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S="bbbcccdddaaa"
assert Solution().numberOfLines(widths,S)==[2,4]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
assert Solution().numberOfLines(widths,S)==[3,60]

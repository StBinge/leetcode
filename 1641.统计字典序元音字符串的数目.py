#
# @lc app=leetcode.cn id=1641 lang=python3
#
# [1641] 统计字典序元音字符串的数目
#

from sbw import *
# @lc code=start
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n+4,4)


# @lc code=end
assert Solution().countVowelStrings(33) == 66045
assert Solution().countVowelStrings(2) == 15
assert Solution().countVowelStrings(1) == 5

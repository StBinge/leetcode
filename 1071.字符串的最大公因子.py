#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ''
        return str1[:math.gcd(len(str1),len(str2))]


# @lc code=end
assert Solution().gcdOfStrings(str1 = "LEET", str2 = "CODE")==''
assert Solution().gcdOfStrings(str1 = "ABCABC", str2 = "ABC")=='ABC'
assert Solution().gcdOfStrings(str1 = "ABABAB", str2 = "ABAB")=='AB'

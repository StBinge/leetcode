#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum([ord(c) for c in t])- sum([ord(c) for c in s]))

# @lc code=end

assert Solution().findTheDifference('abcd','abcde')=='e'
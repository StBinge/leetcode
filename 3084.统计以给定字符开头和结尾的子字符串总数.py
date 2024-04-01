#
# @lc app=leetcode.cn id=3084 lang=python3
#
# [3084] 统计以给定字符开头和结尾的子字符串总数
#

# @lc code=start
# import math
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt=s.count(c)
        return (1+cnt)*cnt//2
# @lc code=end
assert Solution().countSubstrings(s = "zzz", c = "z")==6
assert Solution().countSubstrings(s = "abada", c = "a")==6

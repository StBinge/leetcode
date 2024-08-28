#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#


# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ret = -1
        d = {}
        for i, c in enumerate(s):
            if c in d:
                ret = max(ret, i - d[c] - 1)
            else:
                d[c] = i
        return ret


# @lc code=end
assert Solution().maxLengthBetweenEqualCharacters("abca") == 2
assert Solution().maxLengthBetweenEqualCharacters("aa") == 0

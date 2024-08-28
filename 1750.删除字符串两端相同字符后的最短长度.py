#
# @lc app=leetcode.cn id=1750 lang=python3
#
# [1750] 删除字符串两端相同字符后的最短长度
#


# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            l+=1
            r-=1
            while l <= r and s[l] == s[l-1]:
                l+=1
            while l <= r and s[r] == s[r+1]:
                r -= 1

        return r - l + 1


# @lc code=end
assert Solution().minimumLength("aabccabba") == 3
assert Solution().minimumLength("cabaabac") == 0
assert Solution().minimumLength("ca") == 2

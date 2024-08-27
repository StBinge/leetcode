#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#


# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        nums = [0] * 10
        ord0 = ord("0")
        for ch in s:
            code = ord(ch) - ord0
            if code < 10:
                nums[code] = 1
        for i in range(8, -1, -1):
            nums[i] += nums[i + 1]
            if nums[i] == 2:
                return i
        return -1


# @lc code=end
assert Solution().secondHighest("ck077") == 0
assert Solution().secondHighest("abc1111") == -1
assert Solution().secondHighest("dfa12321afd") == 2

#
# @lc app=leetcode.cn id=1869 lang=python3
#
# [1869] 哪种连续子字符串更长
#


# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        one = 1
        zero = 0
        if s[0] == "0":
            one = 0
            zero = 1
        mx_one = one
        mx_zero = zero
        for i in range(1, len(s)):
            if s[i] == "1":
                one += 1
                mx_zero = max(mx_zero, zero)
                zero = 0
            else:
                zero += 1
                mx_one = max(mx_one, one)
                one = 0
        return max(mx_one, one) > max(mx_zero, zero)


# @lc code=end
assert Solution().checkZeroOnes("110100010")==False
assert Solution().checkZeroOnes("1101")

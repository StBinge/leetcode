#
# @lc app=leetcode.cn id=1837 lang=python3
#
# [1837] K 进制表示下的各位数字总和
#


# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ret = 0
        while n:
            n,m=divmod(n,k)
            ret+=m
        return ret


# @lc code=end
assert Solution().sumBase(10, 10) == 1
assert Solution().sumBase(34, 6) == 9

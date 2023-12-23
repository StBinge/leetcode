#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#
from sbw import *


# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for i in num:
            n = n * 10 + i

        n += k
        ret = []
        while n:
            ret.append(n % 10)
            n //= 10
        return ret[::-1]


# @lc code=end
num = [0]
k = 10000
ret = [1, 0, 0, 0, 0]
assert Solution().addToArrayForm(num, k) == ret

num = [2, 1, 5]
k = 806
ret = [1, 0, 2, 1]
assert Solution().addToArrayForm(num, k) == ret

num = [2, 7, 4]
k = 181
ret = [4, 5, 5]
assert Solution().addToArrayForm(num, k) == ret


num = [1, 2, 0, 0]
k = 34
ret = [1, 2, 3, 4]
assert Solution().addToArrayForm(num, k) == ret

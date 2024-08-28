#
# @lc app=leetcode.cn id=1734 lang=python3
#
# [1734] 解码异或后的排列
#
from sbw import *

# @lc code=start
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        N = len(encoded)
        odd = 0
        for i in range(1, N, 2):
            odd ^= encoded[i]
        total = 0
        for n in range(1, N + 2):
            total ^= n
        ret = [0] * (N + 1)
        ret[0] = total ^ odd
        for i in range(1, N + 1):
            ret[i] = ret[i-1] ^ encoded[i - 1]
        return ret


# @lc code=end
assert Solution().decode([3, 1]) == [1, 2, 3]

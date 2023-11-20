#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1 比特与 2 比特字符
#
from typing import List


# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        L = len(bits)
        idx = L - 2
        while idx >= 0 and bits[idx]:
            idx -= 1
        return (L - idx) % 2 == 0


# @lc code=end
bits = [1, 0, 0]
assert Solution().isOneBitCharacter(bits)

bits = [1, 1, 1, 0]
assert Solution().isOneBitCharacter(bits) == False

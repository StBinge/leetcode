#
# @lc app=leetcode.cn id=1860 lang=python3
#
# [1860] 增长的内存泄露
#
from sbw import *


# @lc code=start
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        time = 1
        while memory1 >= time or memory2 >= time:
            if memory1 >= memory2:
                memory1 -= time
            else:
                memory2 -= time
            time += 1
        return [time, memory1, memory2]


# @lc code=end
assert Solution().memLeak(memory1 = 8, memory2 = 11) == [6,0,4]
assert Solution().memLeak(memory1=2, memory2=2) == [3, 1, 0]

#
# @lc app=leetcode.cn id=面试题 05.06 lang=python3
# @lcpr version=30204
#
# [面试题 05.06] 整数转换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        if A<0:
            A&=0xffffffff
        if B<0:
            B&=0xffffffff
        return (A^B).bit_count()
# @lc code=end

assert Solution().convertInteger(826966453,-729934991)==14

#
# @lcpr case=start
# 29 （或者0b11101）\n15（或者0b01111）\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#


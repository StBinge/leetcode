#
# @lc app=leetcode.cn id=面试题 17.01 lang=python3
# @lcpr version=30204
#
# [面试题 17.01] 不用加号的加法
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1

class Solution:
    def add(self, a: int, b: int) -> int:
        a %= MASK1
        b %= MASK1
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:  # 负数
            return ~((a ^ MASK2) ^ MASK3)
        else:  # 正数
            return a

# @lc code=end
assert Solution().add(4,5)==9
assert Solution().add(1,1)==2


#
# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#


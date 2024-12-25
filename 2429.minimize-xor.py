#
# @lc app=leetcode.cn id=2429 lang=python3
# @lcpr version=30204
#
# [2429] 最小异或
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt2 = num2.bit_count()
        cnt1 = num1.bit_count()
        while cnt2 < cnt1:
            num1 &= num1 - 1
            cnt2 += 1
        while cnt2 > cnt1:
            num1 |= num1 + 1
            cnt2 -= 1
        return num1


# @lc code=end
assert Solution().minimizeXor(25, 72) == 24
assert Solution().minimizeXor(1, 12) == 3
assert Solution().minimizeXor(3, 5) == 3


#
# @lcpr case=start
# 3\n5\n
# @lcpr case=end

# @lcpr case=start
# 1\n12\n
# @lcpr case=end

#

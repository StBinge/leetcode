#
# @lc app=leetcode.cn id=LCR 133 lang=python3
# @lcpr version=30204
#
# [LCR 133] 位 1 的个数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
# @lc code=end



#
# @lcpr case=start
# 11 (控制台输入 00000000000000000000000000001011)\n
# @lcpr case=end

# @lcpr case=start
# 128 (控制台输入 00000000000000000000000010000000)\n
# @lcpr case=end

# @lcpr case=start
# -3）\n
# @lcpr case=end

#


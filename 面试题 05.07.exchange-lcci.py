#
# @lc app=leetcode.cn id=面试题 05.07 lang=python3
# @lcpr version=30204
#
# [面试题 05.07] 配对交换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def exchangeBits(self, num: int) -> int:
        mask=0x55555555
        return (num&mask)<<1 | ((num>>1) & mask)


# @lc code=end
assert Solution().exchangeBits(3)==3
assert Solution().exchangeBits(1)==2


#
# @lcpr case=start
# 3\n
# @lcpr case=end

#


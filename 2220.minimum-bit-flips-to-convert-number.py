#
# @lc app=leetcode.cn id=2220 lang=python3
# @lcpr version=30204
#
# [2220] 转换数字的最少位翻转次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
        
# @lc code=end

assert Solution().minBitFlips(10,7)==3

#
# @lcpr case=start
# 10\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n4\n
# @lcpr case=end

#


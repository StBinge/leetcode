#
# @lc app=leetcode.cn id=面试题 16.07 lang=python3
# @lcpr version=30204
#
# [面试题 16.07] 最大数值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximum(self, a: int, b: int) -> int:
        return (math.isqrt((a-b)**2)+a+b)//2
# @lc code=end



#
# @lcpr case=start
# 1\n2\n
# @lcpr case=end

#


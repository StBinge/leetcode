#
# @lc app=leetcode.cn id=面试题 16.05 lang=python3
# @lcpr version=30204
#
# [面试题 16.05] 阶乘尾数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret= 0
        while n:
            n//=5
            ret+=n
        return ret
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

#


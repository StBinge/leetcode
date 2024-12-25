#
# @lc app=leetcode.cn id=2894 lang=python3
# @lcpr version=30204
#
# [2894] 分类求和并作差
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        tot=(1+n)*n//2
        k=n//m
        return tot-(1+k)*k*m
# @lc code=end



#
# @lcpr case=start
# 10\n3\n
# @lcpr case=end

# @lcpr case=start
# 5\n6\n
# @lcpr case=end

# @lcpr case=start
# 5\n1\n
# @lcpr case=end

#


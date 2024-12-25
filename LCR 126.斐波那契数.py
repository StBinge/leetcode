#
# @lc app=leetcode.cn id=LCR 126 lang=python3
# @lcpr version=30204
#
# [LCR 126] 斐波那契数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        f0=0
        f1=1
        for i in range(2,n+1):
            f0,f1=f1,(f0+f1)%(10**9+7)
        return f1
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#


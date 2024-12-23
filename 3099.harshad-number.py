#
# @lc app=leetcode.cn id=3099 lang=python3
# @lcpr version=30204
#
# [3099] 哈沙德数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        ret=0
        y=x
        while x:
            x,m=divmod(x,10)
            ret+=m
        return ret if y%ret==0 else -1
# @lc code=end



#
# @lcpr case=start
# 18\n
# @lcpr case=end

# @lcpr case=start
# 23\n
# @lcpr case=end

#


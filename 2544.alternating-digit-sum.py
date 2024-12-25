#
# @lc app=leetcode.cn id=2544 lang=python3
# @lcpr version=30204
#
# [2544] 交替数字和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits=[]
        while n:
            n,m=divmod(n,10)
            digits.append(m)
        ret=0
        flag=1
        for d in reversed(digits):
            ret+=d*flag
            flag*=-1
        return ret
# @lc code=end



#
# @lcpr case=start
# 521\n
# @lcpr case=end

# @lcpr case=start
# 111\n
# @lcpr case=end

# @lcpr case=start
# 886996\n
# @lcpr case=end

#


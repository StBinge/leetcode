#
# @lc app=leetcode.cn id=2303 lang=python3
# @lcpr version=30204
#
# [2303] 计算应缴税款总额
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ret=0
        pre=0
        for upper,percent in brackets:
            gap=upper-pre
            ret+=min(gap,income)*percent
            income-=gap
            if income<=0:
                break
            pre=upper
        return ret/100
# @lc code=end
assert_answer(2.65,Solution().calculateTax(brackets = [[3,50],[7,10],[12,25]], income = 10))


#
# @lcpr case=start
# [[3,50],[7,10],[12,25]]\n10\n
# @lcpr case=end

# @lcpr case=start
# [[1,0],[4,25],[5,50]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[2,50]]\n0\n
# @lcpr case=end

#


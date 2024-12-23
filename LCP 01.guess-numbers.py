#
# @lc app=leetcode.cn id=LCP 01 lang=python3
# @lcpr version=30204
#
# [LCP 01] 猜数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(x==y for x,y in zip(guess,answer))
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,3]\n[3,2,1]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=3232 lang=python3
# @lcpr version=30204
#
# [3232] 判断是否可以赢得数字游戏
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        x=y=0
        for n in nums:
            if n<10:
                x+=n
            else:
                y+=n
        return x!=y
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,10]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,14]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,25]\n
# @lcpr case=end

#


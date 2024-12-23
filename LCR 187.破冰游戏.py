#
# @lc app=leetcode.cn id=LCR 187 lang=python3
# @lcpr version=30204
#
# [LCR 187] 破冰游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        f=0
        for i in range(2,num+1):
            f=(f+target)%i
        return f
# @lc code=end



#
# @lcpr case=start
# 7\n4\n
# @lcpr case=end

# @lcpr case=start
# 12\n5\n
# @lcpr case=end

#


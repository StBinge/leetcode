#
# @lc app=leetcode.cn id=2660 lang=python3
# @lcpr version=30204
#
# [2660] 保龄球游戏的获胜者
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calc(player:list):
            ret=0
            double=-1
            for i,cnt in enumerate(player):
                if i<=double:
                    ret+=cnt*2
                else:
                    ret+=cnt
                if cnt==10:
                    double=i+2
            return ret
        
        s1=calc(player1)
        s2=calc(player2)
        if s1>s2:
            return 1
        elif s1<s2:
            return 2
        return 0
# @lc code=end



#
# @lcpr case=start
# [5,10,3,2]\n[6,5,7,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,5,7,6]\n[8,10,10,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3]\n[4,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,10,10,10,10]\n[10,10,10,10,1,1,1]\n
# @lcpr case=end

#


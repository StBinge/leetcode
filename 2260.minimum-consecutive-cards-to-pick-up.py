#
# @lc app=leetcode.cn id=2260 lang=python3
# @lcpr version=30204
#
# [2260] 必须拿起的最小连续卡牌数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        pre_pos={}
        ret=float('inf')
        for i,x in enumerate(cards):
            pre=pre_pos.get(x,-10**7)
            ret=min(ret,i-pre+1)
            pre_pos[x]=i
        return ret if ret<10**6 else -1
# @lc code=end



#
# @lcpr case=start
# [3,4,2,3,4,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,5,3]\n
# @lcpr case=end

#


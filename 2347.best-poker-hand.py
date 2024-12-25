#
# @lc app=leetcode.cn id=2347 lang=python3
# @lcpr version=30204
#
# [2347] 最好的扑克手牌
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suit_cnt=Counter(suits)
        if len(suit_cnt)==1:
            return 'Flush'
        rank_cnt=Counter(ranks)
        mx=max(rank_cnt.values())
        if mx>=3:
            return 'Three of a Kind'
        if mx==2:
            return "Pair"
        return 'High Card'
# @lc code=end



#
# @lcpr case=start
# [13,2,3,1,9]\n["a","a","a","a","a"]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,2,4,4]\n["d","a","a","b","c"]\n
# @lcpr case=end

# @lcpr case=start
# [10,10,2,12,9]\n["a","b","c","a","d"]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=2410 lang=python3
# @lcpr version=30204
#
# [2410] 运动员和训练师的最大匹配数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        ret=0
        pid=0
        pn=len(players)
        for t in trainers:
            while pid<pn and players[pid]>t:
                pid+=1
            if pid==pn:
                return ret
            ret+=1
            pid+=1
        return ret
# @lc code=end
assert Solution().matchPlayersAndTrainers([4,7,9],[8,2,5,8])==2


#
# @lcpr case=start
# [4,7,9]\n[8,2,5,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n[10]\n
# @lcpr case=end

#


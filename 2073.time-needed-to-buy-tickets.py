#
# @lc app=leetcode.cn id=2073 lang=python3
# @lcpr version=30204
#
# [2073] 买票需要的时间
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ret=0
        for i in range(len(tickets)):
            if i<=k:
                ret+=min(tickets[i],tickets[k])
            else:
                ret+=min(tickets[k]-1,tickets[i])
        return ret

# @lc code=end
assert Solution().timeRequiredToBuy([84,49,5,24,70,77,87,8],3)==154


#
# @lcpr case=start
# [2,3,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,1]\n0\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=3185 lang=python3
# @lcpr version=30204
#
# [3185] 构成整天的下标对数目 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        mods=defaultdict(int)
        ret=0
        for h in hours:
            m=h%24
            ret+=mods[(24-m)%24]
            mods[m]+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [12,12,30,24,24]\n
# @lcpr case=end

# @lcpr case=start
# [72,48,24,3]\n
# @lcpr case=end

#


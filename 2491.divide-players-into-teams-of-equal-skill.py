#
# @lc app=leetcode.cn id=2491 lang=python3
# @lcpr version=30204
#
# [2491] 划分技能点相等的团队
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s=sum(skill)
        N=len(skill)//2
        if s%N:
            return -1
        cnt=Counter(skill)
        ret=0
        avg=s//N
        for k,v in cnt.items():
            if v!=cnt[avg-k]:
                return -1
            ret+=(avg-k)*k*v
        return ret//2
# @lc code=end



#
# @lcpr case=start
# [3,2,5,1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3]\n
# @lcpr case=end

#


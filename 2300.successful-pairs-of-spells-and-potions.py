#
# @lc app=leetcode.cn id=2300 lang=python3
# @lcpr version=30204
#
# [2300] 咒语和药水的成功对数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        sorted_spell_idx=sorted(range(len(spells)),key=spells.__getitem__,reverse=True)
        ret=[0]*len(spells)
        N=len(potions)
        lo=0
        for idx in sorted_spell_idx:
            s=spells[idx]
            p=math.ceil(success/s)
            pidx=bisect_left(potions,p,lo=lo)
            ret[idx]=N-pidx
            lo=pidx
        return ret
# @lc code=end
assert Solution().successfulPairs([3,1,2],[8,5,8],16)==[2,0,2]
assert Solution().successfulPairs([5,1,3],[1,2,3,4,5],7)==[4,0,3]


#
# @lcpr case=start
# [5,1,3]\n[1,2,3,4,5]\n7\n
# @lcpr case=end

# @lcpr case=start
# [3,1,2]\n[8,5,8]\n16\n
# @lcpr case=end

#


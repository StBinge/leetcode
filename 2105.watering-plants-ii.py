#
# @lc app=leetcode.cn id=2105 lang=python3
# @lcpr version=30204
#
# [2105] 给植物浇水 II
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        N=len(plants)
        ret=0
        vala=capacityA
        for i in range(N//2):
            if vala<plants[i]:
                vala=capacityA
                ret+=1
            vala-=plants[i]
        
        valb=capacityB
        for i in range(N//2):
            if valb<plants[-i-1]:
                valb=capacityB
                ret+=1
            valb-=plants[-i-1]
        if N&1 and (plants[N//2]>max(vala,valb)):
            ret+=1
        return ret

# @lc code=end
assert Solution().minimumRefill([2,2,3,3],5,5)==1


#
# @lcpr case=start
# [2,2,3,3]\n5\n5\n
# @lcpr case=end

# @lcpr case=start
# [2,2,3,3]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n10\n8\n
# @lcpr case=end

#


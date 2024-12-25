#
# @lc app=leetcode.cn id=2717 lang=python3
# @lcpr version=30204
#
# [2717] 半有序排列
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        p1=pn=0
        N=len(nums)
        for i,n in enumerate(nums):
            if n==1:
                p1=i
            elif n==N:
                pn=i
        ret=p1+N-1-pn
        if p1>pn:
            ret-=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,1,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,4,2,5]\n
# @lcpr case=end

#


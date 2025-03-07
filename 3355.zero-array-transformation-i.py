#
# @lc app=leetcode.cn id=3355 lang=python3
# @lcpr version=30204
#
# [3355] 零数组变换 I
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N=len(nums)
        difs=[0]*(N+1)
        for l,r in queries:
            difs[l]+=1
            difs[r+1]-=1
        
        cur=0
        for n,d in zip(nums,difs):
            cur+=d
            if n>cur:
                return False
        return True
# @lc code=end
assert Solution().isZeroArray([4,3,2,1],[[1,3],[0,2]])==False
assert Solution().isZeroArray([1,0,1],[[0,2]])


#
# @lcpr case=start
# [1,0,1]\n[[0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n[[1,3],[0,2]]\n
# @lcpr case=end

#


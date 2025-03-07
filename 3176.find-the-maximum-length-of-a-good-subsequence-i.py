#
# @lc app=leetcode.cn id=3176 lang=python3
# @lcpr version=30204
#
# [3176] 求出最长好子序列 I
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        fs={}
        mx=[0]*(k+2)
        for x in nums:
            f=fs.setdefault(x,[0]*(k+1))
            for j in range(k,-1,-1):
                f[j]=max(f[j],mx[j])+1                
                mx[j+1]=max(mx[j+1],f[j])

        return mx[-1]
        


# @lc code=end
assert Solution().maximumLength([3,27,24],3) == 3
assert Solution().maximumLength([39,39,38,38],0) == 2
assert Solution().maximumLength([30,30,29],0) == 2
assert Solution().maximumLength(nums=[1, 2, 3, 4, 5, 1], k=0) == 2
assert Solution().maximumLength(nums=[1, 2, 1, 1, 3], k=2) == 4


#
# @lcpr case=start
# [1,2,1,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,1]\n0\n
# @lcpr case=end

#

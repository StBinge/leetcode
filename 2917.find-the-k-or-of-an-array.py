#
# @lc app=leetcode.cn id=2917 lang=python3
# @lcpr version=30204
#
# [2917] 找出数组中的 K-or 值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits=[0]*32
        for n in nums:
            for i in range(32):
                bits[i]+=n&1
                n>>=1
        ret=0
        for i in range(31,-1,-1):
            ret=(ret<<1)+(bits[i]>=k)
        return ret
                
# @lc code=end
assert Solution().findKOr([7,12,9,8,9,15],4)==9


#
# @lcpr case=start
# [7,12,9,8,9,15]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,12,1,11,4,5]\n6\n
# @lcpr case=end

# @lcpr case=start
# [10,8,5,9,11,6,8]\n1\n
# @lcpr case=end

#


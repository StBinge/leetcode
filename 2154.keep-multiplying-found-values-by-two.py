#
# @lc app=leetcode.cn id=2154 lang=python3
# @lcpr version=30204
#
# [2154] 将找到的值乘以 2
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mask=0
        for n in nums:
            k,m=divmod(n,original)
            if m==0 and k & (k-1)==0:
                mask |= k
        
        mask=~mask
        return original*(mask & (-mask))
# @lc code=end


#
# @lcpr case=start
# [5,3,6,1,12]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9]\n4\n
# @lcpr case=end

#


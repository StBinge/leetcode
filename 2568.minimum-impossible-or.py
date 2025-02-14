#
# @lc app=leetcode.cn id=2568 lang=python3
# @lcpr version=30204
#
# [2568] 最小无法得到的或值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        mask=0
        for n in nums:
            if n&n-1==0:
                mask|=n
        mask=~mask
        return mask&-mask
        

# @lc code=end
assert Solution().minImpossibleOR([1,2])==4
assert Solution().minImpossibleOR([5,3,2])==1


#
# @lcpr case=start
# [2,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,3,2]\n
# @lcpr case=end

#


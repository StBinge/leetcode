#
# @lc app=leetcode.cn id=2815 lang=python3
# @lcpr version=30204
#
# [2815] 数组中的最大数对和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_bits=[float('-inf')]*10
        ret=-1
        for n in nums:
            x=n
            mx=0
            while x:
                x,m=divmod(x,10)
                mx=max(mx,m)
            ret=max(ret,max_bits[mx]+n)
            max_bits[mx]=max(max_bits[mx],n)
        return ret
        
# @lc code=end
assert Solution().maxSum( [51,71,17,24,42])==88


#
# @lcpr case=start
# [51,71,17,24,42]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#


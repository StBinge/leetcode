#
# @lc app=leetcode.cn id=2447 lang=python3
# @lcpr version=30204
#
# [2447] 最大公因数等于 K 的子数组数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ret=0
        left=0
        g=nums[0]
        for right,n in enumerate(nums):
            if n%k!=0:
                left=right+1
                g=nums[right+1]
            g=math.gcd(g,nums[right])
            if g==k:
                
# @lc code=end



#
# @lcpr case=start
# [9,3,1,2,6,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4]\n7\n
# @lcpr case=end

#


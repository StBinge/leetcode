#
# @lc app=leetcode.cn id=2918 lang=python3
# @lcpr version=30204
#
# [2918] 数组的最小相等和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1=nums1.count(0)
        s1=sum(nums1)
        z2=nums2.count(0)
        s2=sum(nums2)

        if z1==0 and s1<z2+s2:
            return -1
        if z2==0 and s2<z1+s1:
            return -1
        return max(s1+z1,s2+z2)

# @lc code=end



#
# @lcpr case=start
# [3,2,0,1,0]\n[6,5,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,2,0]\n[1,4]\n
# @lcpr case=end

#


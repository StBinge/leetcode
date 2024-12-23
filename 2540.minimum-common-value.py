#
# @lc app=leetcode.cn id=2540 lang=python3
# @lcpr version=30204
#
# [2540] 最小公共值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i1=i2=0
        n1=len(nums1)
        n2=len(nums2)
        while i1<n1 and i2<n2:
            if nums1[i1]==nums2[i2]:
                return nums1[i1]
            if nums1[i1]<nums2[i2]:
                i1+=1
            else:
                i2+=1
        return -1

# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[2,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,6]\n[2,3,4,5]\n
# @lcpr case=end

#


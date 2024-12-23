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
        s1=sum(nums1)
        zero1=nums1.count(0)
        s2=sum(nums2)
        zero2=nums2.count(0)
        if (zero1==0 and s1<s2+zero2) or (zero2==0 and s2<s1+zero1):
            return -1
        return max(s1+zero1,s2+zero2)
# @lc code=end
assert Solution().minSum([2,0,2,0],[1,4])==-1


#
# @lcpr case=start
# [3,2,0,1,0]\n[6,5,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,2,0]\n[1,4]\n
# @lcpr case=end

#


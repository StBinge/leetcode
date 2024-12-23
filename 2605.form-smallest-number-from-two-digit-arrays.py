#
# @lc app=leetcode.cn id=2605 lang=python3
# @lcpr version=30204
#
# [2605] 从两个数字数组里生成最小数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1=set(nums1)
        s2=set(nums2)
        s=s1&s2
        if s:
            return min(s)
        m1=min(nums1)
        m2=min(nums2)
        return min(m1*10+m2,m2*10+m1)
# @lc code=end



#
# @lcpr case=start
# [4,1,3]\n[5,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,5,2,6]\n[3,1,7]\n
# @lcpr case=end

#


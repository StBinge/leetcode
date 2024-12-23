#
# @lc app=leetcode.cn id=2425 lang=python3
# @lcpr version=30204
#
# [2425] 所有数对的异或和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ret=0
        xor=lambda x,y:x^y
        if len(nums1)&1:
            ret=reduce(xor,nums2)
        if len(nums2)&1:
            ret^=reduce(xor,nums1)
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n[10,2,5,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=2956 lang=python3
# @lcpr version=30204
#
# [2956] 找到两个数组中的公共元素
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1=Counter(nums1)
        cnt2=Counter(nums2)
        ret1=sum(v for k,v in cnt1.items() if k in cnt2)
        ret2=sum(v for k,v in cnt2.items() if k in cnt1)
        return [ret1,ret2]
# @lc code=end



#
# @lcpr case=start
# [2,3,2]\n[1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,3,1]\n[2,2,5,2,3,6]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,2,3]\n[1,5]\n
# @lcpr case=end

#


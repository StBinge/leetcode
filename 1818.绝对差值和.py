#
# @lc app=leetcode.cn id=1818 lang=python3
#
# [1818] 绝对差值和
#
from sbw import *
# @lc code=start
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums1)
        sorted_nums1=sorted(nums1)
        ret=0
        max_alter=0
        for x,y in zip(nums1,nums2):
            dif=abs(x-y)
            ret+=dif
            idx=bisect_left(sorted_nums1,y)
            if idx<N:
                min_dif=sorted_nums1[idx]-y
                max_alter=max(max_alter,dif-min_dif)
            if idx>0:
                min_dif=y-sorted_nums1[idx-1]
                max_alter=max(max_alter,dif-min_dif)
        return (ret-max_alter)%(10**9+7)

        


# @lc code=end
assert Solution().minAbsoluteSumDiff(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4])==20
assert Solution().minAbsoluteSumDiff(nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10])==0
assert Solution().minAbsoluteSumDiff(nums1 = [1,7,5], nums2 = [2,3,5])==3

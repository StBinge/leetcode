#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#
from sbw import *


# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)
        if N1 > N2 * 6 or N2 > N1 * 6:
            return -1
        cnt=[0]*8
        dif=0
        for n in nums1:
            dif+=n
            cnt[n]+=1
        for n in nums2:
            dif-=n
            cnt[7-n]+=1
        if dif<0:
            dif=-dif
        elif dif>0:
            cnt.reverse()
        elif dif==0:
            return 0
        ret = 0
        for i in range(1, 6):
            gap = 6 - i
            if cnt[i] * gap >= dif:
                return ret + (dif - 1) // gap + 1
            else:
                ret += cnt[i]
                dif -= cnt[i] * gap
        return ret

# @lc code=end
assert Solution().minOperations(nums1 = [6,6], nums2 = [1]) == 3
assert Solution().minOperations(nums1=[1, 1, 1, 1, 1, 1, 1], nums2=[6]) == -1
assert Solution().minOperations(nums1=[1, 2, 3, 4, 5, 6], nums2=[1, 1, 2, 2, 2, 2]) == 3

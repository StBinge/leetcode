#
# @lc app=leetcode.cn id=1537 lang=python3
#
# [1537] 最大得分
#
from sbw import *
# @lc code=start
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        pre=0
        Mod=10**9+7
        cur1=cur2=0
        i1,i2=0,0
        L1,L2=len(nums1),len(nums2)
        while i1<L1 and i2<L2:
            x,y=nums1[i1],nums2[i2]
            if x<y:
                cur1+=x
                i1+=1
            elif x>y:
                cur2+=y
                i2+=1
            else:
                pre+=max(cur1,cur2)+x
                i1+=1
                i2+=1
                cur1=cur2=0
                pre%=Mod
        cur1+=sum(nums1[i1:])
        cur2+=sum(nums2[i2:])
        pre+=max(cur1,cur2)
        return pre%Mod
# @lc code=end
assert Solution().maxSum(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10])==40
assert Solution().maxSum(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10])==40
assert Solution().maxSum(nums1 = [1,3,5,7,9], nums2 = [3,5,100])==109
assert Solution().maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9])==30

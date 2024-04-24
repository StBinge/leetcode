#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#
from sbw import *
# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0]>k:
            return k
        arr.append(10000)
        L=len(arr)
        l,r=0,L-1
        while l<r:
            mid=(l+r)>>1
            x=arr[mid]
            if x-(mid+1)>=k:
                r=mid
            else:
                l=mid+1
        return arr[l-1]+(k-(arr[l-1]-l))
# @lc code=end
assert Solution().findKthPositive([2],1)==1
assert Solution().findKthPositive(arr = [1,2,3,4], k = 2)==6
assert Solution().findKthPositive(arr = [2,3,4,7,11], k = 5)==9

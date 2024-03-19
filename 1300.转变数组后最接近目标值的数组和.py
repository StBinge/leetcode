#
# @lc app=leetcode.cn id=1300 lang=python3
#
# [1300] 转变数组后最接近目标值的数组和
#
from sbw import *
# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        presums=[0]
        for n in arr:
            presums.append(n+presums[-1])
        s=0
        L=len(arr)
        l,r=0,L
        while l<r:
            mid=(l+r)>>1
            if presums[mid]+arr[mid]*(L-mid)<=target:
                l=mid+1
            else:
                r=mid
        idx=l
        if idx==0:
            avg= target//L
            if abs(target-avg*L) <= abs(target-(avg+1)*L):
                return avg
            else:
                return avg+1
        elif idx==L:
            return arr[-1]
        s=target-sum(arr[:idx])
        l=arr[idx-1]
        r=arr[idx]
        cnt=L-idx
        while l<r:
            mid=(l+r)>>1
            if mid*cnt<=s:
                l=mid+1
            else:
                r=mid
        if abs(s-(l-1)*cnt)<=abs(s-l*cnt):
            return l-1
        else:
            return l
# @lc code=end
assert Solution().findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803)==11361
assert Solution().findBestValue(arr = [2,3,5], target = 10)==5
assert Solution().findBestValue(arr = [4,9,3], target = 10)==3

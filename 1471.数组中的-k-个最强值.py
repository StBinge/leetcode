#
# @lc app=leetcode.cn id=1471 lang=python3
#
# [1471] 数组中的 k 个最强值
#
from sbw import *
# @lc code=start
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        L=len(arr)
        mid=arr[(L-1)//2]

        
        ret=[]
        l=0
        r=L-1
        for i in range(k):
            left=mid-arr[l]
            right=arr[r]-mid
            if left>right:
                ret.append(arr[l])
                l+=1
            else:
                ret.append(arr[r])
                r-=1
        return ret
# @lc code=end
assert sorted(Solution().getStrongest([-7,22,17,3],2))==sorted([22,17])
assert sorted(Solution().getStrongest(arr = [6,7,11,7,6,8], k = 5))==sorted([11,8,6,6,7])
assert sorted(Solution().getStrongest(arr = [1,1,3,5,5], k = 2))==sorted([5,5])
assert sorted(Solution().getStrongest(arr = [1,2,3,4,5], k = 2))==sorted([5,1])

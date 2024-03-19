#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#
from sbw import *
# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=sum(arr[:k-1])
        ret=0
        for i in range(k-1,len(arr)):
            s+=arr[i]
            if s/k>=threshold:
                ret+=1
            s-=arr[i-k+1]
        return ret
# @lc code=end
assert Solution().numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5)==6
assert Solution().numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4)==3

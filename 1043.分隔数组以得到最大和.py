#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#
from sbw import *
# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        L=len(arr)
        f=[0]*(L+1)
        for i in range(1,L+1):
            ma=arr[i-1]
            for j in range(i-1,max(-1,i-k-1),-1):
                f[i]=max(f[i],f[j]+ma*(i-j))
                if j>0:
                    ma=max(ma,arr[j-1])
        return f[-1]
# @lc code=end
assert Solution().maxSumAfterPartitioning([1],1)==1

arr = [1,4,1,5,7,3,6,1,9,9,3]
k = 4
assert Solution().maxSumAfterPartitioning(arr,k)==83

arr = [1,15,7,9,2,5,10]
k = 3
assert Solution().maxSumAfterPartitioning(arr,k)==84

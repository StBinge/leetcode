#
# @lc app=leetcode.cn id=1846 lang=python3
#
# [1846] 减小和重新排列数组后的最大元素
#
from sbw import *


# @lc code=start
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N=len(arr)
        cnt=[0]*(1+N)
        for x in arr:
            cnt[min(x,N)]+=1
        miss=0
        for i in range(1,N+1):
            if cnt[i]==0:
                miss+=1
            else:
                miss-=min(cnt[i]-1,miss)
        return N-miss

# @lc code=end
assert Solution().maximumElementAfterDecrementingAndRearranging([100, 1, 1000]) == 3
assert Solution().maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]) == 5
assert (
    Solution().maximumElementAfterDecrementingAndRearranging(arr=[2, 2, 1, 2, 1]) == 2
)

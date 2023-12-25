#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#
from sbw import *
# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        buckets=Counter(nums)
        ret=sum(nums)
        for i in range(-100,0):
            if buckets[i]==0:
                continue
            ops=min(k,buckets[i])
            ret-=i*2*ops
            buckets[-i]+=ops
            k-=ops
            if k==0:
                break
        if k%2 and buckets[0]==0:
            for i in range(1,101):
                if buckets[i]==0:
                    continue
                ret-=i*2
                break
        return ret

# @lc code=end
nums = [-4,-2,-3]
k = 4
assert Solution().largestSumAfterKNegations(nums,k)==5


nums = [2,-3,-1,5,-4]
k = 2
assert Solution().largestSumAfterKNegations(nums,k)==13

nums = [3,-1,0,2]
k = 3
assert Solution().largestSumAfterKNegations(nums,k)==6

nums = [4,2,3]
k = 1
assert Solution().largestSumAfterKNegations(nums,k)==5

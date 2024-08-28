#
# @lc app=leetcode.cn id=1726 lang=python3
#
# [1726] 同积元组
#
from sbw import *
# @lc code=start
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter=defaultdict(int)
        N=len(nums)
        ret=0
        for i in range(N):
            for j in range(i+1,N):
                prod=nums[i]*nums[j]
                ret+=8*counter[prod]
                counter[prod]+=1
        return ret

# @lc code=end
assert Solution().tupleSameProduct([1,2,4,5,10])==16
assert Solution().tupleSameProduct(nums = [2,3,4,6])==8

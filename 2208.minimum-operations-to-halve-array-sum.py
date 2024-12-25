#
# @lc app=leetcode.cn id=2208 lang=python3
# @lcpr version=30204
#
# [2208] 将数组和减半的最少操作次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from fractions import Fraction
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=-(nums[i]<<20)
        
        heapq.heapify(nums)
        target=sum(nums)>>1
        ret=0
        while target<0:
            half=nums[0]//2
            target-=half
            heapq.heapreplace(nums,half)
            ret+=1
        return ret

        

# @lc code=end
assert Solution().halveArray([1])==1
assert Solution().halveArray([5,19,8,1])==3


#
# @lcpr case=start
# [5,19,8,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,8,20]\n
# @lcpr case=end

#


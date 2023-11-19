#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的 k-diff 数对
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        L=len(nums)
        y=0
        ret=0
        for i in range(L):
            if i==0 or nums[i]!=nums[i-1]:
                while y<L and (nums[y]-nums[i]<k or y<=i):
                    y+=1
                if y<L and nums[y]-nums[i]==k:
                    ret+=1


        return ret
# @lc code=end
assert Solution().findPairs([3,1,4,1,5],2)==2
assert Solution().findPairs([1,1,1,2,2],0)==2
assert Solution().findPairs([1,2,3,4,5],5)==0
assert Solution().findPairs([1, 3, 1, 5, 4],0)==1
assert Solution().findPairs([1, 2, 3, 4, 5],1)==4

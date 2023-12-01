#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
from typing import List
# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeat=-1
        for n in nums:
            if nums[abs(n)-1]<0:
                repeat=abs(n)
            else:
                nums[abs(n)-1]*=-1
        miss=-1
        for i,n in enumerate(nums):
            if n>0:
                miss=i+1
                break
        return [repeat,miss]

# @lc code=end

assert Solution().findErrorNums([1,2,2,4])==[2,3]
assert Solution().findErrorNums([1,1])==[1,2]
#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 K 小的数对距离
#
from typing import List
# @lc code=start
import bisect
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # L=len(nums)
        nums.sort()
        def count(mid:int):
            cnt=0
            i=0
            for j,n in enumerate(nums):
                while i<j and n-nums[i]>mid:
                    i+=1
                cnt+=j-i
            return cnt
        return bisect.bisect_left(range(nums[-1]-nums[0]),k,key=count)
# @lc code=end
nums = [1,6,1]
k = 3
assert Solution().smallestDistancePair(nums,k)==5
nums = [1,3,1]
k = 1
assert Solution().smallestDistancePair(nums,k)==0
nums = [1,1,1]
k = 2
assert Solution().smallestDistancePair(nums,k)==0


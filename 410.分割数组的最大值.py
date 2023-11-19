#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
from typing import List
# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left,right=max(nums),sum(nums)
        while left<right:
            mid=(left+right)//2
            total,cnt=0,1
            for n in nums:
                if total+n>mid:
                    cnt+=1
                    total=n
                    if cnt>k:
                        left=mid+1
                        break
                else:
                    total+=n
            else:
                right=mid
        return left
         
# @lc code=end
nums = [7,2,5,10,8]
m = 2
assert Solution().splitArray(nums,m)==18

nums = [1,2,3,4,5]
m = 2
assert Solution().splitArray(nums,m)==9
nums = [1,4,4]
m = 3
assert Solution().splitArray(nums,m)==4

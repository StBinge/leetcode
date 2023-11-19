#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#
from typing import List
# @lc code=start

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        def rob(sums:list):
            if len(sums)==1:
                return sums[0]
            first,second=sums[0],max(sums[0],sums[1])
            for i in range(2,len(sums)):
                first,second=second,max(second,first+sums[i])
            return second
        ret=0
        nums.sort()
        sums=[nums[0]]
        for i in range(1,len(nums)):
            cur=nums[i]
            pre=nums[i-1]
            if cur==pre:
                sums[-1]+=cur
            elif cur==pre+1:
                sums.append(cur)
            else:
                ret+=rob(sums)
                sums=[cur]
        ret+=rob(sums)
        return ret
# @lc code=end
nums=[8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]
assert Solution().deleteAndEarn(nums)==61

nums=[8,7,3,8,1,4,10,10,10,2]
assert Solution().deleteAndEarn(nums)==52
assert Solution().deleteAndEarn([2,3,4])==6
nums = [2,2,3,3,3,4]
assert Solution().deleteAndEarn(nums)==9
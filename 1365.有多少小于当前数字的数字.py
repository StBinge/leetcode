#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#
from sbw import *
# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt=Counter(nums)
        keys=sorted(cnt.keys())
        counter={keys[0]:0}
        for i in range(1,len(keys)):
            counter[keys[i]]=counter[keys[i-1]]+cnt[keys[i-1]]
        ret=[0]*len(nums)
        for i in range(len(nums)):
            ret[i]=counter[nums[i]]
        return ret


# @lc code=end
assert Solution().smallerNumbersThanCurrent([7,7,7,7])==[0,0,0,0]
assert Solution().smallerNumbersThanCurrent([6,5,4,8])==[2,1,0,3]
assert Solution().smallerNumbersThanCurrent([8,1,2,2,3])==[4,0,1,1,3]

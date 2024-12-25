#
# @lc app=leetcode.cn id=2903 lang=python3
# @lcpr version=30204
#
# [2903] 找出满足差值条件的下标 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        N=len(nums)
        if indexDifference>=N:
            return [-1,-1]
        mi=mx=0

        for i in range(indexDifference,N):
            pre_idx=i-indexDifference
            if nums[pre_idx]<nums[mi]:
                mi=pre_idx
            if nums[pre_idx]>nums[mx]:
                mx=pre_idx
            if abs(nums[mi]-nums[i])>=valueDifference:
                return [mi,i]
            if abs(nums[mx]-nums[i])>=valueDifference:
                return [mx,i]
        return [-1,-1]
# @lc code=end
def test(nums,d1,d2,ret):
    x,y=Solution().findIndices(nums,d1,d2)
    if x==-1:
        return [x,y]==ret
    return abs(x-y)>=d1 and abs(nums[x]-nums[y])>=d2

test([8],0,2,[-1,-1])
test([7,5,6,2],2,2,[0,3])


#
# @lcpr case=start
# [5,1,4,1]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n0\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n2\n4\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=2172 lang=python3
# @lcpr version=30204
#
# [2172] 数组的最大与和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        ret=0
        slots=[2]*(numSlots+1)
        N=len(nums)
        for i in range(N):
            n=nums[i]
            if n<=numSlots and slots[n]:
                ret+=n
                slots[n]-=1
                nums[i]=0
        nums.sort(reverse=True)
        for n in nums:
            if n==0:
                break
            val=0
            target=0
            for x in range(numSlots,-1,-1):
                if slots[x]==0:
                    continue
                if x&n>=val:
                    target=x
                    val=x&n
            slots[target]-=1
            ret+=target
        return ret


# @lc code=end
assert Solution().maximumANDSum([14,7,9,8,2,4,11,1,9],8)==40
assert Solution().maximumANDSum([1,2,3,4,5,6],3)==9


#
# @lcpr case=start
# [1,2,3,4,5,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,3,10,4,7,1]\n9\n
# @lcpr case=end

#


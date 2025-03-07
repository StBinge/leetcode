#
# @lc app=leetcode.cn id=3326 lang=python3
# @lcpr version=30204
#
# [3326] 使数组非递减的最少除法操作次数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
Mx=1_000_001
LPF=[0]*Mx
for i in range(2,Mx):
    for j in range(i,Mx,i):
        if LPF[j]==0:
            LPF[j]=i
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        ret=0
        N=len(nums)
        for i in range(N-2,-1,-1):
            if nums[i]>nums[i+1]:
                nums[i]=LPF[nums[i]]
                if nums[i]>nums[i+1]:
                    return -1
                else:
                    ret+=1
        
        return ret


# @lc code=end
assert Solution().minOperations([5,51,25])==-1
assert Solution().minOperations([105,11])==1
assert Solution().minOperations( [1,1,1,1])==0
assert Solution().minOperations([7,7,6])==-1
assert Solution().minOperations([25,7])==1


#
# @lcpr case=start
# [25,7]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

#


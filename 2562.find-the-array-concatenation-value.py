#
# @lc app=leetcode.cn id=2562 lang=python3
# @lcpr version=30204
#
# [2562] 找出数组的串联值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        ret=0
        while left<right:
            n1=nums[left]
            n2=nums[right]
            l=len(str(n2))
            ret+=n1*(10**l)+n2
            left+=1
            right-=1
        if left==right:
            ret+=nums[left]
        return ret
# @lc code=end



#
# @lcpr case=start
# [7,52,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [5,14,13,8,12]\n
# @lcpr case=end

#


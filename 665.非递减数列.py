#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#
from typing import List
# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # pre=float('-inf')
        changed=False
        L=len(nums)
        for i in range(L-1):
            x,y=nums[i],nums[i+1]
            if x>y:
                if changed:
                    return False
                changed=True
                if i>0 and y<nums[i-1]:
                    nums[i+1]=x
        

                    
        return True
# @lc code=end
assert Solution().checkPossibility([-1,4,2,3])==True
assert Solution().checkPossibility([3,4,2,3])==False
assert Solution().checkPossibility([5,7,1,8])
assert Solution().checkPossibility([4,1,2])
assert Solution().checkPossibility([4,3,1])==False

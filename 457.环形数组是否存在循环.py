#
# @lc app=leetcode.cn id=457 lang=python3
#
# [457] 环形数组是否存在循环
#
from typing import List
# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        idx=0
        N=len(nums)
        for i in range(N):
            if nums[i]>1000:
                continue
            idx=i
            mark=1001+i
            forward=nums[idx]>0
            # cnt=1
            while nums[idx]<=1000:
                step=nums[idx]
                if abs(step)%N==0:
                    break
                if (step>0) ^ forward:
                    break
                nums[idx]=mark
                nxt=(idx+step)%N
                if nums[nxt]==mark:
                    return True
                idx=nxt
                # cnt+=1
        return False



# @lc code=end

assert Solution().circularArrayLoop([-2,-3,-9])==False
assert Solution().circularArrayLoop([-1,-2,-3,-4,-5])==False
assert Solution().circularArrayLoop([1,-1,5,1,4])
assert Solution().circularArrayLoop([2,-1,1,2,2])
assert Solution().circularArrayLoop([-1,2])==False
assert Solution().circularArrayLoop([-2,1,-1,-2,-2])==False
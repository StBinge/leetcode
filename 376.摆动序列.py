#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#
from typing import List
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N=len(nums)
        # if N==1:
        #     return 1
        # if N==2:
        #     return 2 if nums[0]!=nums[1] else 1
            
        if N ==1:
            return 1
        pre_dif=nums[1]-nums[0]
        ret=2 if pre_dif!=0 else 1
        for i in range(2,N):
            dif=nums[i]-nums[i-1]
            if (dif>0 and pre_dif<=0) or (dif<0 and pre_dif>=0):
                ret+=1
                pre_dif=dif
        return ret

# @lc code=end
assert Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9])==2
assert Solution().wiggleMaxLength([1,7,4,9,2,5])==6
assert Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])==7

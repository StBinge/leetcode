#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#
from sbw import *
# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ret=[]
        for left,right in zip(l,r):
            mi,ma=min(nums[left:right+1]),max(nums[left:right+1])
            if mi==ma:
                ret.append(True)
                continue
            l=right-left
            if (ma-mi)%l:
                ret.append(False)
                continue
            
            d=(ma-mi)//l
            vis=[False]*(l+1)
            for i in range(left,right+1):
                if (nums[i]-mi)%d:
                    ret.append(False)
                    break
                idx=(nums[i]-mi)//d
                if vis[idx]:
                    ret.append(False)
                    break
                vis[idx]=True
            else:
                ret.append(True)
        return ret

# @lc code=end
assert Solution().checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10])==eval_list_str('[false,true,false,false,true,true]')
assert Solution().checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])==eval_list_str('[true,false,true]')

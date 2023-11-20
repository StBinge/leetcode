#
# @lc app=leetcode.cn id=565 lang=python3
#
# [565] 数组嵌套
#
from typing import List
# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        L=len(nums)
        # vis=[False]*L
        ret=0
        for i in range(L):
            cnt=0
            while nums[i]<L:
                cnt+=1
                nxt=nums[i]
                nums[i]=L
                i=nxt
            ret=max(ret,cnt)
        return ret
# @lc code=end

assert Solution().arrayNesting([5,4,0,3,1,6,2])==4
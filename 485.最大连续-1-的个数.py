#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#
from typing import List
# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret=0
        cnt=0
        for i in nums:
            if i==1:
                cnt+=1
            else:
                ret=max(ret,cnt)
                cnt=0
        return max(cnt,ret)
# @lc code=end

assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])==3
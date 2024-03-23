#
# @lc app=leetcode.cn id=1313 lang=python3
#
# [1313] 解压缩编码列表
#
from sbw import *
# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret=[]
        for i in range(0,len(nums),2):
            ret.extend([nums[i+1]]*nums[i])
        return ret
# @lc code=end

assert Solution().decompressRLElist([1,2,3,4])==[2,4,4,4]
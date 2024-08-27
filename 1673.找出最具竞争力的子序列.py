#
# @lc app=leetcode.cn id=1673 lang=python3
#
# [1673] 找出最具竞争力的子序列
#
from sbw import *


# @lc code=start
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        if N==k:
            return nums
        ret=[]
        for i,n in enumerate(nums):
            while ret and ret[-1]>n and len(ret)+N-i>k:
                ret.pop()
            ret.append(n)
        return ret[:k]



# @lc code=end
assert Solution().mostCompetitive([84,10,71,23,66,61,62,64,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71],24) == [10,23,61,62,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71]
assert Solution().mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2],3) == [8,80,2]
assert Solution().mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4) == [2,3,3,4]
assert Solution().mostCompetitive(nums=[3, 5, 2, 6], k=2) == [2, 6]

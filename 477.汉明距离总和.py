#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#
from typing import List
# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ret=0
        N=len(nums)
        for i in range(30):
            cnt=sum([(n>>i) & 1 for n in nums])
            ret+=cnt*(N-cnt)
        return ret
# @lc code=end
assert Solution().totalHammingDistance([4,14,2])==6
assert Solution().totalHammingDistance([4,14,4])==4

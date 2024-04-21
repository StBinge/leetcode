#
# @lc app=leetcode.cn id=1526 lang=python3
#
# [1526] 形成目标数组的子数组最少增加次数
#
from sbw import *
# @lc code=start
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ret=target[0]
        for x,y in pairwise(target):
            ret+=max(y-x,0)
        return ret
# @lc code=end
assert Solution().minNumberOperations([1,1,1,1])==1
assert Solution().minNumberOperations([3,1,5,4,2])==7
assert Solution().minNumberOperations([3,1,1,2])==4
assert Solution().minNumberOperations([1,2,3,2,1])==3

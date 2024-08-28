#
# @lc app=leetcode.cn id=1521 lang=python3
#
# [1521] 找到最接近目标值的函数值
#
from sbw import *
# @lc code=start
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        if target==-10**9:
            return 0
        ret=abs(-10**9-target)
        # L=len(arr)
        valid={arr[0]}
        for n in arr:
            valid={n& pre for pre in valid} | {n}
            ret=min(ret,min(abs(x-target) for x in valid))
        return ret

# @lc code=end
assert Solution().closestToTarget(arr = [9,12,3,7,15], target = 5)==2

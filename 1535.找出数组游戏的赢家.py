#
# @lc app=leetcode.cn id=1535 lang=python3
#
# [1535] 找出数组游戏的赢家
#

from sbw import *


# @lc code=start
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        pre,s=arr[0],0
        for i in range(1,len(arr)):
            if s==k:
                return pre
            if pre>arr[i]:
                s+=1
            else:
                pre=arr[i]
                s=1
        return pre


# @lc code=end
assert Solution().getWinner([1,25,35,42,68,70],1) == 25
assert Solution().getWinner(arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000) == 99
assert Solution().getWinner(arr=[1, 9, 8, 2, 3, 7, 6, 4, 5], k=7) == 9
assert Solution().getWinner(arr=[3, 2, 1], k=10) == 3
assert Solution().getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2) == 5

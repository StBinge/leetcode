#
# @lc app=leetcode.cn id=769 lang=python3
#
# [769] 最多能完成排序的块
#
from typing import List
# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt=0
        Max=0
        for i,n in enumerate(arr):
            Max=max(Max,n)
            if Max==i:
                cnt+=1
        return cnt

# @lc code=end
arr = [4,3,2,1,0]
assert Solution().maxChunksToSorted(arr)==1
arr=[1,0,2,3,4]
assert Solution().maxChunksToSorted(arr)==4
assert Solution().maxChunksToSorted([0])==1

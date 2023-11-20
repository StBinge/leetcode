#
# @lc app=leetcode.cn id=826 lang=python3
#
# [826] 安排工作以达到最大收益
#
from typing import List
# @lc code=start
import bisect
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs=sorted(zip(difficulty,profit))
        ret=idx=best=0
        l=len(jobs)
        for skill in sorted(worker):            
            while idx<l and skill>=jobs[idx][0]:
                best=max(best,jobs[idx][1])
                idx+=1
            ret+=best
        return ret

# @lc code=end
difficulty = [85,47,57]
profit = [24,66,99]
worker = [40,25,25]
ret=0
assert Solution().maxProfitAssignment(difficulty,profit,worker)==ret

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
ret=100
assert Solution().maxProfitAssignment(difficulty,profit,worker)==ret

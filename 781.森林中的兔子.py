#
# @lc app=leetcode.cn id=781 lang=python3
#
# [781] 森林中的兔子
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter=Counter(answers)
        ret=0
        for k,v in counter.items():
            ret+=((k+v)//(k+1))*(k+1)

        return ret
# @lc code=end
answers = [1,1,2]
assert Solution().numRabbits(answers)==5
answers = [10,10,10]
assert Solution().numRabbits(answers)==11

#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
from typing import List
# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret=[None]*n
        for i in range(1,n+1):
            if i%15==0:
                ret[i-1]='FizzBuzz'
            elif i%5==0:
                ret[i-1]='Buzz'
            elif i%3==0:
                ret[i-1]='Fizz'
            else:
                ret[i-1]=str(i)
        return ret
# @lc code=end


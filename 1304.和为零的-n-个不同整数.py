#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的 N 个不同整数
#
from sbw import *
# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret=[]
        for i in range(0,n//2):
            ret.append(i+1)
            ret.append(-1-i)
        if n%2:
            ret.append(0)
        return ret
# @lc code=end
ret= Solution().sumZero(4)
assert sum(ret)==0 and len(set(ret))==4
ret= Solution().sumZero(5)
assert sum(ret)==0 and len(set(ret))==5

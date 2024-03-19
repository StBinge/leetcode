#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#
from sbw import *
# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        memo=set()
        zero_cnt=0
        for n in arr:
            if n==0:
                zero_cnt+=1
                if zero_cnt>1:
                    return True
                continue
            if 2*n in arr or (n%2==0 and n//2 in arr):
                return True
            memo.add(n)
        return False
# @lc code=end
assert Solution().checkIfExist([-2,0,10,-19,4,6,-8])==False
assert Solution().checkIfExist([3,1,7,11])==False
assert Solution().checkIfExist([7,1,14,11])
assert Solution().checkIfExist([10,2,5,3])

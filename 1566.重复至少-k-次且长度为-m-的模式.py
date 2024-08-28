#
# @lc app=leetcode.cn id=1566 lang=python3
#
# [1566] 重复至少 K 次且长度为 M 的模式
#
from sbw import *
# @lc code=start
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n=len(arr)
        if n<m*k:
            return False
        for i in range(n-m*k+1):
            offset=m
            while offset<k*m and arr[i+offset%m]==arr[i+offset]:
                offset+=1
            if offset==k*m:
                return True
        return False

# @lc code=end

assert Solution().containsPattern(arr = [1,2,3,1,2], m = 2, k = 2)==False
assert Solution().containsPattern(arr = [1,2,1,2,1,3], m = 2, k = 3)==False
assert Solution().containsPattern(arr = [1,2,1,2,1,1,1,3], m = 2, k = 2)==True
assert Solution().containsPattern([1,2,4,4,4,4],1,3)==True
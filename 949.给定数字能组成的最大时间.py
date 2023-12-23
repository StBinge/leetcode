#
# @lc app=leetcode.cn id=949 lang=python3
#
# [949] 给定数字能组成的最大时间
#
from sbw import *
# @lc code=start
from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time=-1
        ret=''
        for h1,h2,m1,m2 in permutations(arr):
            h=h1*10+h2
            if h>=24:
                continue
            m=m1*10+m2
            if m>=60:
                continue
            time=h*60+m
            if time>max_time:
                max_time=time
                ret=f'{h1}{h2}:{m1}{m2}'
        return ret
# @lc code=end
assert Solution().largestTimeFromDigits([2,0,6,6])=="06:26"
assert Solution().largestTimeFromDigits([4,2,4,4])==""
assert Solution().largestTimeFromDigits([0,0,1,0])=="10:00"
assert Solution().largestTimeFromDigits([0,0,0,0])=="00:00"
assert Solution().largestTimeFromDigits([5,5,5,5])==""
assert Solution().largestTimeFromDigits([1,2,3,4])=="23:41"

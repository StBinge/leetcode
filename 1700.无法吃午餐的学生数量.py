#
# @lc app=leetcode.cn id=1700 lang=python3
#
# [1700] 无法吃午餐的学生数量
#
from sbw import *
# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt=[0,0]
        for s in students:
            cnt[s]+=1
        for s in sandwiches:
            if cnt[s]==0:
                break
            cnt[s]-=1

        return sum(cnt)
        
# @lc code=end


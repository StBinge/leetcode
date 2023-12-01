#
# @lc app=leetcode.cn id=630 lang=python3
#
# [630] 课程表 III
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        stack=[]
        total=0
        for dur,last in courses:
            if total+dur<=last:
                heapq.heappush(stack,-dur)
                total+=dur
            elif stack and dur<-stack[0]:
                total+=stack[0]+dur
                heapq.heappushpop(stack,-dur)
        return len(stack)
# @lc code=end
courses=[[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]
assert Solution().scheduleCourse(courses)==5

courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
assert Solution().scheduleCourse(courses)==3
courses = [[3,2],[4,3]]
assert Solution().scheduleCourse(courses)==0
assert Solution().scheduleCourse([[1,2]])==1

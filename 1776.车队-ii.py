#
# @lc app=leetcode.cn id=1776 lang=python3
#
# [1776] 车队 II
#
from sbw import *
# @lc code=start
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        N=len(cars)

        speed_change=None
        ret=[-1]*N
        def calc(cur_pos,cur_speed,pre_pos,pre_speed):
            return (pre_pos-cur_pos)/(cur_speed-pre_speed)
        st=[N-1]
        for i in range(N-2,-1,-1):
            while st and (cars[st[-1]][1]>=cars[i][1] or (ret[st[-1]]>0 and ret[st[-1]]<=calc(*cars[i],*cars[st[-1]]))):
                st.pop()
            if st:
                ret[i]=calc(*cars[i],*cars[st[-1]])
            st.append(i)
        return ret

# @lc code=end
ret= Solution().getCollisionTimes([[3,4],[5,4],[6,3],[9,1]])
assert_answer([2.00000,1.00000,1.50000,-1.00000],ret)
ret= Solution().getCollisionTimes([[1,2],[2,1],[4,3],[7,2]])
assert_answer([1.00000,-1.00000,3.00000,-1.00000],ret)
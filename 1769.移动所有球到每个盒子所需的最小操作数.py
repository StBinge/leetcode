#
# @lc app=leetcode.cn id=1769 lang=python3
#
# [1769] 移动所有球到每个盒子所需的最小操作数
#
from sbw import *
# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N=len(boxes)

        ret=[0]*N
        left,right,op=int(boxes[0]),0,0
        for i in range(1,N):
            if boxes[i]=='1':
                right+=1
                op+=i
        ret[0]=op

        for i in range(1,N):
            op+=left-right
            if boxes[i]=='1':
                left+=1
                right-=1
            ret[i]=op
        return ret
# @lc code=end
assert Solution().minOperations('001011')==[11,8,5,4,3,4]
assert Solution().minOperations('110')==[1,1,3]

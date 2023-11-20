#
# @lc app=leetcode.cn id=636 lang=python3
#
# [636] 函数的独占时间
#
from typing import List
# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # if n==1:
        #     return int(logs[-1].split(':')[-1])+1
        ret=[0]*n
        tid_stack=[]
        pre_time=0
        for log in logs:
            parts=log.split(':')
            tid=int(parts[0])
            flag=parts[1][0]
            time=int(parts[2])
            if flag=='e':
                pre_id=tid_stack.pop()
                ret[pre_id]+=time-pre_time+1
                pre_time=time+1
            else:
                if tid_stack:
                    pre_id=tid_stack[-1]
                    ret[pre_id]+=time-pre_time
                tid_stack.append(tid)
                pre_time=time
        return ret


# @lc code=end
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
assert Solution().exclusiveTime(n,logs)==[3,4]

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
assert Solution().exclusiveTime(n,logs)==[8]

n = 1
logs = ["0:start:0","0:end:0"]
assert Solution().exclusiveTime(n,logs)==[1]

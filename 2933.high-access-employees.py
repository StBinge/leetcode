#
# @lc app=leetcode.cn id=2933 lang=python3
# @lcpr version=30204
#
# [2933] 高访问员工
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        times=defaultdict(list)
        for name,st in access_times:
            tick=int(st[:2])*60+int(st[2:])
            times[name].append(tick)
        ret=[]
        for name,ticks in times.items():
            ticks.sort()
            for i in range(2,len(ticks)):
                if ticks[i]-ticks[i-2]<60:
                    ret.append(name)
                    break
        return ret
# @lc code=end



#
# @lcpr case=start
# [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]\n
# @lcpr case=end

# @lcpr case=start
# [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]\n
# @lcpr case=end

# @lcpr case=start
# [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]\n
# @lcpr case=end

#


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
        users=defaultdict(list)
        for user,time in access_times:
            t=int(time[:2])*60+int(time[2:])
            users[user].append(t)
        ret=[]
        for user,times in users.items():
            if len(times)<3:
                continue
            times.sort()
            if any(times[i]-times[i-2]<60 for i in range(2,len(times))):
                ret.append(user)
                    
        return ret
# @lc code=end
assert sorted(Solution().findHighAccessEmployees([["fnlmbcedu","0052"],["fnlmbcedu","0103"],["fnlmbcedu","0055"]]))==sorted(["fnlmbcedu"])
assert sorted(Solution().findHighAccessEmployees([["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]))==sorted(["c","d"])
assert Solution().findHighAccessEmployees( [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]])==['a']


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


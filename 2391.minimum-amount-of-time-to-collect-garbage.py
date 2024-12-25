#
# @lc app=leetcode.cn id=2391 lang=python3
# @lcpr version=30204
#
# [2391] 收集垃圾的最少总时间
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ret = 0
        vis=set()
        for i in range(len(garbage)-1,0,-1):
            vis.update(garbage[i])
            if len(vis)==3:
                ret+=sum(travel[:i])*3+sum(map(len,garbage[:i+1]))
                return ret
            ret+=travel[i-1]*len(vis)+len(garbage[i])
        return ret+len(garbage[0])


# @lc code=end
assert Solution().garbageCollection(["MMM","PGM","GP"],[3,10])==37
assert Solution().garbageCollection(["G","P","GP","GG"],[2,4,3])==21

#
# @lcpr case=start
# ["G","P","GP","GG"]\n[2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# ["MMM","PGM","GP"]\n[3,10]\n
# @lcpr case=end

#

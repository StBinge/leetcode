#
# @lc app=leetcode.cn id=面试题 16.15 lang=python3
# @lcpr version=30204
#
# [面试题 16.15] 珠玑妙算
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        ret=[0,0]
        cnt1=defaultdict(int)
        cnt2=defaultdict(int)
        for x,y in zip(solution,guess):
            if x==y:
                ret[0]+=1
            else:
                cnt1[x]+=1
                cnt2[y]+=1
        ret[1]=sum(min(cnt1[k],cnt2[k]) for k in cnt2)
        return ret

# @lc code=end



#
# @lcpr case=start
# "RGBY"\n"GGRR"\n
# @lcpr case=end

#


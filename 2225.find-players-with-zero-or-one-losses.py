#
# @lc app=leetcode.cn id=2225 lang=python3
# @lcpr version=30204
#
# [2225] 找出输掉零场或一场比赛的玩家
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnt=defaultdict(int)
        wins=defaultdict(int)
        for w,l in matches:
            cnt[w]+=1
            cnt[l]+=1
            wins[w]+=1
        ret=[[],[]]
        for k in sorted(cnt.keys()):
            ck,wk=cnt[k],wins[k]
            dif=ck-wk
            if dif<2:
                ret[ck-wk].append(k)
        return ret
# @lc code=end
assert Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])==[[1,2,10],[4,5,7,8]]


#
# @lcpr case=start
# [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,3],[1,3],[5,4],[6,4]]\n
# @lcpr case=end

#


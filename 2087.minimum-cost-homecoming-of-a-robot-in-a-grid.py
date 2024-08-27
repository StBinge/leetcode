#
# @lc app=leetcode.cn id=2087 lang=python3
# @lcpr version=30204
#
# [2087] 网格图中机器人回家的最小代价
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sr,sc=startPos
        hr,hc=homePos
        ret=0
        if sr>hr:
            ret+=sum(rowCosts[hr:sr])
        else:
            ret+=sum(rowCosts[sr+1:hr+1])
        if sc>hc:
            ret+=sum(colCosts[hc:sc])
        else:
            ret+=sum(colCosts[sc+1:hc+1])
        return ret
# @lc code=end
assert Solution().minCost([5,5],[5,2],[7,1,3,3,5,3,22,10,23],[5,5,6,2,0,16])==8
assert Solution().minCost([4,1],[0,2],[6,3,0,8,19,21,10],[0,7,23,15,13,19,12,14])==40
assert Solution().minCost(startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26])==0
assert Solution().minCost(startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7])==18


#
# @lcpr case=start
# [1, 0]\n[2, 3]\n[5, 4, 3]\n[8, 2, 6, 7]\n
# @lcpr case=end

# @lcpr case=start
# [0, 0]\n[0, 0]\n[5]\n[26]\n
# @lcpr case=end

#


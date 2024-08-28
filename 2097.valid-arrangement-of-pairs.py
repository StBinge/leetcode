#
# @lc app=leetcode.cn id=2097 lang=python3
# @lcpr version=30204
#
# [2097] 合法重新排列数对
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        N=len(pairs)
        ends=defaultdict(list)
        starts=defaultdict(list)
        for i,[s,e] in enumerate(pairs):
            starts[s].append(i)
            ends[e].append(i)
        indeg=[0]*N
        outdeg=[0]*N
        
# @lc code=end



#
# @lcpr case=start
# [[5,1],[4,5],[11,9],[9,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[3,2],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,3],[2,1]]\n
# @lcpr case=end

#


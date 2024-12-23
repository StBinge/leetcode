#
# @lc app=leetcode.cn id=2363 lang=python3
# @lcpr version=30204
#
# [2363] 合并相似的物品
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        cnt=defaultdict(int)
        for v,w in items1:
            cnt[v]+=w
        for v,w in items2:
            cnt[v]+=w
        
        return list(sorted(cnt.items()))
# @lc code=end



#
# @lcpr case=start
# [[1,1],[4,5],[3,8]]\n[[3,1],[1,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[3,2],[2,3]]\n[[2,1],[3,2],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[2,2]]\n[[7,1],[2,2],[1,4]]\n
# @lcpr case=end

#


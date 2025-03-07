#
# @lc app=leetcode.cn id=2768 lang=python3
# @lcpr version=30204
#
# [2768] 黑格子的数目
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def countBlackBlocks(
        self, m: int, n: int, coordinates: List[List[int]]
    ) -> List[int]:
        cnt = defaultdict(int)
        for x, y in coordinates:
            if y+1<n and x+1<m:
                cnt[x,y]+=1
            if x > 0 and y+1<n:
                cnt[x - 1, y] += 1
            if y > 0 and x+1<m:
                cnt[x, y - 1] += 1
            if x*y> 0:
                cnt[x - 1, y - 1] += 1



        ret = [0] * 5
        for v in cnt.values():
            ret[v] += 1
        ret[0] = (m-1) * (n-1) - sum(ret)
        return ret


# @lc code=end


assert Solution().countBlackBlocks(22,73,[[11,14],[16,11],[20,5],[5,33],[14,7],[16,60],[0,15],[15,72],[6,60],[9,16],[14,51],[1,52],[18,24],[17,30],[3,4],[19,13],[9,10],[11,40],[15,7],[13,62],[8,41],[12,71],[4,72],[18,7],[1,0],[4,35],[16,33],[7,30],[13,52],[5,1],[15,21],[3,59],[2,41],[4,28]]) == [1387,122,3,0,0]
assert Solution().countBlackBlocks(m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]) == [0,2,2, 0, 0]
assert Solution().countBlackBlocks(m=3, n=3, coordinates=[[0, 0]]) == [3, 1, 0, 0, 0]


#
# @lcpr case=start
# 3\n3\n[[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n[[0,0],[1,1],[0,2]]\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=2271 lang=python3
# @lcpr version=30204
#
# [2271] 毯子覆盖的最多白色砖块数
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        left = 0
        ret = 0
        cover = 0
        for l,r in tiles:
            cover+=r-l+1
            while r-tiles[left][1]+1>carpetLen:
                cover-=tiles[left][1]-tiles[left][0]+1
                left+=1
            uncover=max(r-tiles[left][0]+1 - carpetLen,0)
            ret=max(ret,cover-uncover)

        return ret


# @lc code=end
assert Solution().maximumWhiteTiles(tiles=[[10, 11], [1, 1]], carpetLen=2) == 2
assert (
    Solution().maximumWhiteTiles(
        tiles=[[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], carpetLen=10
    )
    == 9
)


#
# @lcpr case=start
# [[1,5],[10,11],[12,18],[20,25],[30,32]]\n10\n
# @lcpr case=end

# @lcpr case=start
# [[10,11],[1,1]]\n2\n
# @lcpr case=end

#

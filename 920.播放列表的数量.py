#
# @lc app=leetcode.cn id=920 lang=python3
#
# [920] 播放列表的数量
#

# @lc code=start
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
# @lc code=end

#
# @lc app=leetcode.cn id=920 lang=python3
#
# [920] 播放列表的数量
#

# @lc code=start
from functools import lru_cache
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        f=[[0]*(n+1) for _ in range(goal+1)]
        f[0][0]=1
        for i in range(1,goal+1):
            for j in range(1,n+1):
                f[i][j]=f[i-1][j-1]*(n-j+1)
                if j>k:
                    f[i][j]+=f[i-1][j]*(j-k)
                f[i][j]%=10**9+7
        return f[-1][-1]
# @lc code=end
assert Solution().numMusicPlaylists(16,16,4)==789741546

n = 3
goal = 3
k = 1
assert Solution().numMusicPlaylists(n,goal,k)==6

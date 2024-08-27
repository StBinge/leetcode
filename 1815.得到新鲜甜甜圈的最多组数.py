#
# @lc app=leetcode.cn id=1815 lang=python3
#
# [1815] 得到新鲜甜甜圈的最多组数
#
from sbw import *


# @lc code=start
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        ret = 0
        mods = [0] * batchSize
        for g in groups:
            m = g % batchSize
            if m == 0:
                ret += 1
                continue
            if mods[batchSize - m]:
                ret += 1
                mods[batchSize - m] -= 1
            else:
                mods[m] += 1

        @cache
        def dfs(left,cnt:tuple):
            cnt=list(cnt)
            res=0
            for m,v in enumerate(cnt):
                if not v:
                    continue
                cnt[m]-=1
                res=max(res,(left==0)+dfs((left+m+1)%batchSize,tuple(cnt)))
                cnt[m]+=1
            return res
        
        return ret+dfs(0,tuple(mods[1:]))

# @lc code=end
assert Solution().maxHappyGroups(3,[369821235,311690424,74641571,179819879,171396603,274036220]) == 4
assert Solution().maxHappyGroups(batchSize = 4, groups = [1,3,2,5,2,2,1,6]) == 4
assert Solution().maxHappyGroups(batchSize=3, groups=[1, 2, 3, 4, 5, 6]) == 4

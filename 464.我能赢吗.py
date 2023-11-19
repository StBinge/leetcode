#
# @lc app=leetcode.cn id=464 lang=python3
#
# [464] 我能赢吗
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        cache={}
        def dfs(mask,total):
            if (mask,total) in cache:
                return cache[(mask,total)]
            for i in range(maxChoosableInteger):
                if (mask>>i) & 1==1:
                    continue
                if total+i+1>=desiredTotal or not dfs(mask | (1<<i),total+i+1):
                    cache[(mask,total)]=True
                    return True
            cache[(mask,total)]=False
            return False
        
        if maxChoosableInteger>=desiredTotal:
            return True
        if (1+maxChoosableInteger)*maxChoosableInteger/2<desiredTotal:
            return False
        return dfs(0,0)
# @lc code=end

assert Solution().canIWin(10,40)==False
assert Solution().canIWin(4,6)
assert Solution().canIWin(10,11)==False
assert Solution().canIWin(10,0)
assert Solution().canIWin(10,1)
#
# @lc app=leetcode.cn id=818 lang=python3
#
# [818] 赛车
#

# @lc code=start
# from collections import deque
import heapq
# from functools import lru_cache
class Solution:
    def racecar(self, target: int) -> int:
        f=[float('inf')]*(target+1)
        for i in range(1,target+1):
            k=i.bit_length()
            pre_k=(1<<(k-1))-1
            for b in range(k-1):
                back=(1<<b)-1
                f[i]=min(f[i],k-1+b+2+f[i-pre_k+back])
            walk=(1<<k)-1
            if walk==i:
                f[i]=k
            if walk-i<i:
                f[i]=min(f[i],k+1+f[walk-i])
        return f[target]
        

# @lc code=end
assert Solution().racecar(4)==5
exit()
assert Solution().racecar(5)==7
assert Solution().racecar(3)==2
assert Solution().racecar(6)==5

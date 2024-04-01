#
# @lc app=leetcode.cn id=1497 lang=python3
#
# [1497] 检查数组对是否可以被 k 整除
#
from sbw import *
# @lc code=start
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mods=[0]*k
        for n in arr:
            mods[n%k]+=1
        if mods[0]%2:
            return False
        return all(mods[i]==mods[k-i] for i in range(1,k//2+1))
        
# @lc code=end
assert Solution().canArrange(arr = [1,2,3,4,5,6], k = 10)==False
assert Solution().canArrange(arr = [1,2,3,4,5,6], k = 7)
assert Solution().canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5)

#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] 优美的排列 II
#
from typing import List
# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        mid=n-k
        ret=list(range(1,mid))
        i,j=mid,n
        while i<=j:
            if i==j:
                ret.append(i)
                break
            ret.append(i)
            ret.append(j)
            i+=1
            j-=1
        return ret
# @lc code=end

print(Solution().constructArray(10,3))
print(Solution().constructArray(3,2))
print(Solution().constructArray(3,1))

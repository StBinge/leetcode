#
# @lc app=leetcode.cn id=954 lang=python3
#
# [954] 二倍数对数组
#
from sbw import *
# @lc code=start
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt=Counter(arr)
        if cnt[0]%2:
            return False
        for x in sorted(cnt,key=abs):
            if cnt[2*x]<cnt[x]:
                return False
            cnt[2*x]-=cnt[x]
        return True
# @lc code=end
arr = [4,-2,2,-4]
assert Solution().canReorderDoubled(arr)

arr = [3,1,3,6]
assert Solution().canReorderDoubled(arr)==False
arr = [2,1,2,6]
assert Solution().canReorderDoubled(arr)==False

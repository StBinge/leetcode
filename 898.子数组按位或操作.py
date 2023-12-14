#
# @lc app=leetcode.cn id=898 lang=python3
#
# [898] 子数组按位或操作
#
from typing import List


# @lc code=start
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans=set()
        cur={0}
        for x in arr:
            cur={x|y for y in cur} | {x}
            ans|=cur
        return len(ans)


# @lc code=end

assert Solution().subarrayBitwiseORs([1,2,4]) == 6
assert Solution().subarrayBitwiseORs([0]) == 1
assert Solution().subarrayBitwiseORs([1, 1, 2]) == 3

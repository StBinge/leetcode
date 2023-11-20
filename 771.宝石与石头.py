#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s=set(jewels)
        ret=0
        for stone in stones:
            if stone in s:
                ret+=1
        return ret
# @lc code=end


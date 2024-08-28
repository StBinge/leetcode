#
# @lc app=leetcode.cn id=1753 lang=python3
#
# [1753] 移除石子的最大得分
#

# @lc code=start
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ma=max(a,b,c)
        two_sum=a+b+c-ma
        if two_sum<ma:
            return two_sum
        else:
            return (a+b+c)//2
# @lc code=end
assert Solution().maximumScore(1,8,8)==8
assert Solution().maximumScore(4,4,6)==7
assert Solution().maximumScore(2,4,6)==6

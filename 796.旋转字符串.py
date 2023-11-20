#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        return (s+s).find(goal)>=0
# @lc code=end


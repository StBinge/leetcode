#
# @lc app=leetcode.cn id=面试题 10.05 lang=python3
# @lcpr version=30204
#
# [面试题 10.05] 稀疏数组搜索
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for i,word in enumerate(words):
            if not word:
                continue
            if word==s:
                return i
        return -1
# @lc code=end



#
# @lcpr case=start
# ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""]\n"ta"\n
# @lcpr case=end

# @lcpr case=start
# ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""]\n"ball"\n
# @lcpr case=end

#


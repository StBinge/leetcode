#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces=text.count(' ')
        if len(words)==1:
            return words[0]+' '*spaces
        avg,remain=divmod(spaces,len(words)-1)
        return (' '*avg).join(words)+' '*remain

# @lc code=end

assert Solution().reorderSpaces("a")=="a"
assert Solution().reorderSpaces("  this   is  a sentence ")=="this   is   a   sentence"
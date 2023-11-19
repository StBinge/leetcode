#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # L=len(word)
        
        if len(word)>=2 and word[1].isupper() and word[0].islower():
            return False
      
        return all(word[i].islower()==word[1].islower() for i in range(2,len(word)))
        
# @lc code=end

assert Solution().detectCapitalUse('USA')
assert Solution().detectCapitalUse('FlaG')==False
assert Solution().detectCapitalUse('F')
assert Solution().detectCapitalUse('f')
#
# @lc app=leetcode.cn id=2135 lang=python3
# @lcpr version=30204
#
# [2135] 统计追加字母可以获得的单词数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        masks=set()
        for word in startWords:
            mask=0
            for ch in word:
                mask |= 1<<(ord(ch)-ord('a'))
            masks.add(mask)
        
        ret=0
        for word in targetWords:
            mask=0
            for ch in word:
                mask |= 1<<(ord(ch)-ord('a'))
            
            for ch in word:
                if mask^(1<<(ord(ch)-ord('a'))) in masks:
                    ret+=1
                    break
        return ret
# @lc code=end
assert Solution().wordCount(["g","vf","ylpuk","nyf","gdj","j","fyqzg","sizec"],["r","am","jg","umhjo","fov","lujy","b","uz","y"])==2


#
# @lcpr case=start
# ["ant","act","tack"]\n["tack","act","acti"]\n
# @lcpr case=end

# @lcpr case=start
# ["ab","a"]\n["abc","abcd"]\n
# @lcpr case=end

#


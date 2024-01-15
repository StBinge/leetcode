#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#
from sbw import *
# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt=Counter(chars)
        ret=0
        for word in words:
            cnt=Counter(word)
            for k,v in cnt.items():
                if v>chars_cnt[k]:
                    break
            else:
                ret+=len(word)
        return ret
# @lc code=end
assert Solution().countCharacters(words = ["cat","bt","hat","tree"], chars = "atach")==6

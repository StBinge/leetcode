#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#
from sbw import *
# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        maps={c:i for i,c in enumerate(order)}
        for i in range(1,len(words)):
            w1=words[i-1]
            w2=words[i]
            for j in range(min(len(w1),len(w2))):
                if w1[j]==w2[j]:
                    continue
                o1,o2=maps[w1[j]],maps[w2[j]]
                if o1<o2:
                    break
                if o1>o2:
                    return False
            else:
                if len(w1)>len(w2):
                    return False
        return True

# @lc code=end
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
assert Solution().isAlienSorted(words,order)==False

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
assert Solution().isAlienSorted(words,order)==False

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
assert Solution().isAlienSorted(words,order)

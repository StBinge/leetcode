#
# @lc app=leetcode.cn id=916 lang=python3
#
# [916] 单词子集
#
from cv2 import solve
from sbw import *
# @lc code=start

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        pat=Counter()
        for w in words2:
            cnt=Counter(w)
            for k,v in cnt.items():
                pat[k]=max(pat[k],v)

        ret=[]
        for w in words1:
            cnt=Counter(w)
            for k,v in pat.items():
                if cnt[k]<v:
                    break
            else:
                ret.append(w)
        return ret

# @lc code=end
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","oo"]
ret=["facebook","google"]
assert Solution().wordSubsets(words1,words2)==ret

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["l","e"]
ret=["apple","google","leetcode"]
assert Solution().wordSubsets(words1,words2)==ret

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
ret=["facebook","google","leetcode"]
assert Solution().wordSubsets(words1,words2)==ret

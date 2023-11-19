#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

from typing import List
# @lc code=start
import collections
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target={}
        for ch in licensePlate:
            if not ch.isalpha():
                continue
            ch=ch.lower()
            val=target.get(ch,0)+1
            target[ch]=val
        total=sum(target.values())
        ret=''
        for word in words:
            if len(word)<total or (ret and len(word)>=len(ret)):
                continue
            counter=collections.Counter(word)
            for k in target:
                if target[k]>counter[k]:
                    break
            else:
                ret=word
        return ret

# @lc code=end
licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
assert Solution().shortestCompletingWord(licensePlate,words)=='steps'
licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
assert Solution().shortestCompletingWord(licensePlate,words)=='pest'

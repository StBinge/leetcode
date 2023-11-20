#
# @lc app=leetcode.cn id=809 lang=python3
#
# [809] 情感丰富的文字
#
from typing import List
# @lc code=start
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        l1=len(s)
        ret=0
        for word in words:
            i=j=0
            l2=len(word)
            while i<l1 and j<l2:
                if s[i]!=word[j]:
                    break
                cur=s[i]
                cnt1=0
                while i<l1 and s[i]==cur:
                    cnt1+=1
                    i+=1
                cnt2=0
                while j<l2 and word[j]==cur:
                    cnt2+=1
                    j+=1
                if cnt1<cnt2 or (cnt1<3 and cnt1!=cnt2):
                    break
            else:
                if i==l1 and j==l2:
                    ret+=1
        return ret
# @lc code=end
s = "heeellooo"
words = ["hello", "hi", "helo","heeellooo"]
assert Solution().expressiveWords(s,words)==1
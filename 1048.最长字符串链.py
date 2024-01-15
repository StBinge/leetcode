#
# @lc app=leetcode.cn id=1048 lang=python3
#
# [1048] 最长字符串链
#
from sbw import *
# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cnt={}
        words.sort(key=len)
        # s=set(words)
        ret=0
        for word in words:
            cnt[word]=1
            for i in range(len(word)):
                prev=word[:i]+word[i+1:]
                if prev in cnt:
                    cnt[word]=max(cnt[word],cnt[prev]+1)
            ret=max(ret,cnt[word])
        return ret
# @lc code=end
words=["abcd","dbqca"]
assert Solution().longestStrChain(words)==1

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
assert Solution().longestStrChain(words)==5

words = ["a","b","ba","bca","bda","bdca"]
assert Solution().longestStrChain(words)==4

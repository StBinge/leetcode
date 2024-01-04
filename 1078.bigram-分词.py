#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#
from sbw import *
# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ret=[]
        q=deque()
        for word in text.split():
            if len(q)<2:
                q.append(word)
                continue
            if q[0]==first and q[1]==second:
                ret.append(word)
            q.popleft()
            q.append(word)
       
        return ret
# @lc code=end
text="ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk"
first="lnlqhmaohv"
second="ypkk"
assert Solution().findOcurrences(text, first, second)==["ypkk","ypkk"]
assert Solution().findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good")==["girl","student"]

#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#
from sbw import *
# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # counter=[0]*26
        # L=len(words)
        # appers=[[False]*L for _ in range(26)]
        # for word in words:
        #     for c in word:
        #         counter[ord(c)-ord('a')]+=1
        # ret=[]
        # for i,c in counter:
        #     if c>0 and c%L==0:
        counters=[Counter(word) for word in words]
        ret=[]
        for i in range(26):
            c=chr(i+ord('a'))
            cnt=float('inf')
            for counter in counters:
                if counter[c]<cnt:
                    cnt=counter[c]
            if cnt:
                ret.extend([c]*cnt)
        return ret

# @lc code=end
words = ["bella","label","roller"]
ret=["e","l","l"]
assert Solution().commonChars(words)==sorted(ret)

words = ["cool","lock","cook"]
ret=["c","o"]
assert Solution().commonChars(words)==sorted(ret)
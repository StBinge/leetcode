#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#
from sbw import *
# @lc code=start
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def cnt(word:str):
            char='z'
            cnt=0
            for c in word:
                if c==char:
                    cnt+=1
                elif c<char:
                    char=c
                    cnt=1
            return cnt
        count=[0]*12
        for word in words:
            c=cnt(word)
            count[c]+=1
        for i in range(9,-1,-1):
            count[i]+=count[i+1]
        ret=[]

        for q in queries:
            qc=cnt(q)
            ret.append(count[qc+1])
        return ret
# @lc code=end
assert Solution().numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"])==[1,2]
assert Solution().numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"])==[1]

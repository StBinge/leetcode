#
# @lc app=leetcode.cn id=466 lang=python3
#
# [466] 统计重复个数
#

# @lc code=start
from collections import Counter
from math import gcd
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        recall={}
        index=0
        cnt1=0
        L2=len(s2)
        while True:
            cnt1+=1
            for ch in s1:
                if ch==s2[index%L2]:
                    index+=1
            if cnt1==n1:
                return index//L2//n2
            if (index % L2) in recall:
                preloop=recall[index%L2]
                inloop=[cnt1-preloop[0],index//L2-preloop[1]]
                break
            recall[index % L2]=[cnt1,index//L2]

        ans=preloop[1]+(n1-preloop[0])//inloop[0]*inloop[1]
        rest=(n1-preloop[0])%inloop[0]
        index%=L2
        for _ in range(rest):
            for ch in s1:
                if ch==s2[index%L2]:
                    index+=1
        return (ans+index//L2)//n2


# @lc code=end

assert Solution().getMaxRepetitions('acb',4,'ab',2)==2
assert Solution().getMaxRepetitions('acb',1,'acb',1)==1
assert Solution().getMaxRepetitions('aaa',3,'aa',1)==4
#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#

# @lc code=start
class KMP:
    def __init__(self,pattern:str) -> None:
        L=len(pattern)
        next=[0]*L
        k=0
        for i in range(1,L):
            while k>0 and pattern[i]!=pattern[k]:
                k=next[k-1]
            if pattern[i]==pattern[k]:
                k+=1
            next[i]=k
        self.next=next
        self.pattern=pattern

    def find(self,s:str):
        L=len(s)
        N=len(self.pattern)
        i,j=0,0
        # start=i
        while i<L+j:
            while j>0 and self.pattern[j]!=s[i%L]:
                j=self.next[j-1]
            # if j==0:
            #     start=i
            if self.pattern[j]==s[i%L]:
                i+=1
                j+=1
                if j==N:
                    return i-j
            else:
                i+=1
        return -1

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # La=len(a)
        # Lb=len(b)
        # if Lb>La:
        #     base=(Lb-1)//La+1
        #     a*=base

        # idx=(2*a).find(b)
        # if idx<0:
        #     return -1
        # return (idx+Lb-1)//La + 1
        kmp=KMP(b)
        idx=kmp.find(a)
        if idx<0:
            return -1
        return (idx+len(b)-1)//len(a)+1

# @lc code=end
# kmp=KMP('abcabe')
# idx=kmp.find('eabcabcab')
# pass
a="abcd"
b="cdabcdacdabcda"
assert Solution().repeatedStringMatch(a,b)==-1

a="abaabaa"
b="abaababaab"

assert Solution().repeatedStringMatch(a,b)==-1
assert Solution().repeatedStringMatch('aaac','aac')==1

a = "abcd"
b = "cdabcdab"
assert Solution().repeatedStringMatch(a,b)==3
a = "abc"
b = "wxyz"
assert Solution().repeatedStringMatch(a,b)==-1

assert Solution().repeatedStringMatch('a','aa')==2
assert Solution().repeatedStringMatch('a','a')==1

#abcd abcdabcd
#__cd abcdacdabcda
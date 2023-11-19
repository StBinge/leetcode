#
# @lc app=leetcode.cn id=843 lang=python3
#
# [843] 猜猜这个单词
#
from typing import List
class Master:
    def __init__(self,secret,times) -> None:
        self.secret=secret
        self.times=times
    def guess(self, word: str) -> int:
        if self.times==0:
            raise 'No times left'
        self.times-=1
        ret=0
        for i in range(6):
            if word[i]==self.secret[i]:
                ret+=1
        return ret
# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n=len(words)
        # samelarity=[{} for i in range(n)]
        samelarity=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                s=0
                for k in range(6):
                    if words[i][k]==words[j][k]:
                        s+=1
                samelarity[i][j]=s
                samelarity[j][i]=s
        flags=[False]*n
        while True:
            bound=n+1
            canidate=0
            for i in range(n):
                if flags[i]:
                    continue
                dis=[0]*7
                for s in samelarity[i]:
                    dis[s]+=1
                m=max(dis)
                if m<bound:
                    bound=m
                    canidate=i

            flags[canidate]=True
            g=master.guess(words[canidate])
            if g==6:
                return
            for j,s in enumerate(samelarity[canidate]):
                if s!=g:
                    flags[j]=True
        
# class Solution:
#     def findSecretWord(self, wordlist, master):
#         def distance(x,y):
#             ans = 0
#             for i in range(6):
#                 if x[i] == y[i]:
#                     ans += 1
#             return ans
#         """
#         :type wordlist: List[Str]
#         :type master: Master
#         :rtype: None
#         """
#         dp = [0] * len(wordlist) #记录是否被排除
#         for g in range(10):
#             #寻找下一个猜测单词
#             candidate = 0
#             vote = float('inf')
#             for i in range(len(wordlist)):
#                 if dp[i] == 0:
#                     dis = [0] * 7
#                     for j in range(len(wordlist)):
#                         if j != i and dp[j] == 0:
#                             dis[distance(wordlist[i],wordlist[j])] += 1
#                     if max(dis) < vote:
#                         candidate = i
#                         vote = max(dis)
#             #猜测
#             dp[candidate] = 1
#             tmp = master.guess(wordlist[candidate])
#             #排除不可能的单词
#             for i in range(len(wordlist)):
#                 if dp[i] == 0 and distance(wordlist[candidate],wordlist[i]) != tmp:
#                     dp[i] = 1

      

# @lc code=end
master=Master('zzzzzz',30)
words=["aaaaaa","bbbbbb","cccccc","dddddd","eeeeee","ffffff","gggggg","hhhhhh","iiiiii","jjjjjj","kkkkkk","llllll","mmmmmm","nnnnnn","oooooo","pppppp","qqqqqq","rrrrrr","ssssss","tttttt","uuuuuu","vvvvvv","wwwwww","xxxxxx","yyyyyy","zzzzzz"]
Solution().findSecretWord(words,master)

master=Master('azzzzz',10)
words=["abcdef","acdefg","adefgh","aefghi","afghij","aghijk","ahijkl","aijklm","ajklmn","aklmno","almnoz","anopqr","azzzzz"]
Solution().findSecretWord(words,master)

master=Master('hbaczn',10)
words=["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]

Solution().findSecretWord(words,master)
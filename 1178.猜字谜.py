#
# @lc app=leetcode.cn id=1178 lang=python3
#
# [1178] 猜字谜
#
from sbw import *
# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.slots:dict[str,TrieNode]=dict()
        self.freq=0
    
    def add(self,word:str):
        cur=self
        for ch in sorted(set(word)):
            cur=cur.slots.setdefault(ch,TrieNode())
        cur.freq+=1
    
    def __find(self,chars:str,req:str,index:int):
        if index==7:
            return self.freq
        ret=0
        ch=chars[index]
        if ch in self.slots:
            ret+=self.slots[ch].__find(chars,req,index+1)
        if ch!=req:
            ret+=self.__find(chars,req,index+1)
        return ret

    def find(self,puzzle:str):
        p=sorted(puzzle)
        req=puzzle[0]
        return self.__find(p,req,0)


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        root=TrieNode()
        for word in words:
            root.add(word)
        ret=[]
        for p in puzzles:
            ret.append(root.find(p))
        return ret
# @lc code=end
assert Solution().findNumOfValidWords(words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"])==[1,1,3,2,4,0]

#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#
from typing import List
# @lc code=start
class DicTree:
    def __init__(self) -> None:
        self.slots={}
        self.end=''
    
    def insert(self,word:str):
        cur=self
        for c in word:
            cur=cur.slots.setdefault(c,DicTree())
        cur.end=word
    
    def match(self,word:str):
        cur=self
        for c in word:
            if c not in cur.slots:
                return ''
            cur=cur.slots[c]
            if cur.end:
                return cur.end

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictree=DicTree()
        for root in dictionary:
            dictree.insert(root)
        
        ret=sentence.split(' ')
        for i in range(len(ret)):
            r=dictree.match(ret[i])
            if r:
                ret[i]=r
        return ' '.join(ret)

# @lc code=end

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
ret="the cat was rat by the bat"
assert Solution().replaceWords(dictionary,sentence)==ret

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
ret="a a b c"
assert Solution().replaceWords(dictionary,sentence)==ret

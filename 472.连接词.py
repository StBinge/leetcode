#
# @lc app=leetcode.cn id=472 lang=python3
#
# [472] 连接词
#
from typing import List
# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.slots:dict[str,Trie]={}
        self.is_end=False
    
    def insert(self,word):
        cur=self
        for ch in word:
            cur=cur.slots.setdefault(ch,Trie())
        cur.is_end=True
    
    def find(self,word,index,vis:list[bool]):
        if len(word)==index:
            return True
        cur=self
        if vis[index]:
            return False
        vis[index]=True
        for i in range(index,len(word)):
            ch=word[i]
            cur=cur.slots.get(ch,None)
            if not cur:
                return False
            if cur.is_end and self.find(word,i+1,vis):
                return True
        return False
                

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        root=Trie()
        ret=[]
        for word in words:
            if root.find(word,0,[False]*len(word)):
                ret.append(word)
            else:
                root.insert(word)
        return ret

# @lc code=end
words = ["cat","dog","catdog"]
print(Solution().findAllConcatenatedWordsInADict(words))

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(Solution().findAllConcatenatedWordsInADict(words))
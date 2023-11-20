#
# @lc app=leetcode.cn id=676 lang=python3
#
# [676] 实现一个魔法字典
#
from typing import List
# @lc code=start
class DictTree:
    def __init__(self) -> None:
        self.slots=[None]*26
        self.isword=False
    
    def insert(self,word:str):
        cur=self
        for ch in word:
            idx=ord(ch)-ord('a')
            if not cur.slots[idx]:
                cur.slots[idx]=DictTree()
            cur=cur.slots[idx]
        cur.isword=True
    
    def search(self,word:str, cur_idx,modified=False):
        if cur_idx==len(word):
            return self.isword and modified
        ch=word[cur_idx]
        slot_id=ord(ch)-ord('a')
        if self.slots[slot_id] and self.slots[slot_id].search(word,cur_idx+1,modified):
            return True
        
        if not modified:
            for i in range(26):
                if i==slot_id or self.slots[i]==None:
                    continue
                if self.slots[i].search(word,cur_idx+1,True):
                    return True
        return False
        

    
    # def delete(self,word:str):
    #     cur=self
    #     for ch in word:
    #         idx=ord(ch)-ord('a')
    #         cur=cur.slots[idx]
    #     cur.isword=False

class MagicDictionary:

    def __init__(self):
        self.dict=DictTree()
        self.lengths=set()
        # self.words=None

    def buildDict(self, dictionary: List[str]) -> None:
        # self.words=set(dictionary)
        for word in dictionary:
            self.lengths.add(len(word))
            self.dict.insert(word)

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.lengths:
            return False
        
        return self.dict.search(searchWord,0,False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end
magicDictionary=MagicDictionary()


magicDictionary.buildDict(["hello", "leetcode",'hallo'])
assert magicDictionary.search("hello")
assert magicDictionary.search("hhllo")
assert not magicDictionary.search("hell")
assert not magicDictionary.search("leetcoded")
assert magicDictionary.search("leetcodo")
magicDictionary=MagicDictionary()

magicDictionary.buildDict(["a", "b",'ab'])
assert magicDictionary.search("a")
assert magicDictionary.search("b")
assert magicDictionary.search("c")
assert magicDictionary.search("d")
assert magicDictionary.search("e")
assert not magicDictionary.search("ab")
assert not magicDictionary.search("ba")
assert not magicDictionary.search("abc")

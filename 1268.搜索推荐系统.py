#
# @lc app=leetcode.cn id=1268 lang=python3
#
# [1268] 搜索推荐系统
#
from sbw import *
# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.slots:list[TrieNode]=[None]*26
        self.ending=-1
    
    def add(self,word:str,idx:int):
        cur=self
        for c in word:
            order=ord(c)-ord('a')
            if not cur.slots[order]:
                cur.slots[order]=TrieNode()
            cur=cur.slots[order]
        cur.ending=idx
    
    # def search(self,char:str):
    #     node= self.slots[ord(char)-ord('a')]
    
    def get_words(self,ret:list):
        if len(ret)==3:
            return
        if self.ending!=-1:
            ret.append(self.ending)
        for nxt in self.slots:
            if nxt:
                nxt.get_words(ret)
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ret=[]
        products.sort()
        pre=''
        lo=0
        for c in searchWord:
            pre+=c
            lo=bisect_left(products,pre,lo=lo)
            ret.append([word for word in products[lo:lo+3] if word.startswith(pre)])
        return ret
# @lc code=end
assert Solution().suggestedProducts(products = ["havana"], searchWord = "tatiana")==[[],[],[],[],[],[],[]]
assert Solution().suggestedProducts(products = ["bags","baggage","banner","box","cloths"], searchWord = "bags")==[
    ["baggage","bags","banner"],
    ["baggage","bags","banner"],
    ["baggage","bags"],
    ["bags"]]
assert Solution().suggestedProducts(products = ["havana"], searchWord = "havana")==[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

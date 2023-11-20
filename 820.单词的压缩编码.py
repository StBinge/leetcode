#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#
from typing import List
# @lc code=start
class DicTree:
    def __init__(self) -> None:
        self.slots={}
        self.ending=-1
    
    def insert_reverse(self,word:str):
        cur=self
        for c in reversed(word):
            cur=cur.slots.setdefault(c,DicTree())
            # cur.ending=idx
            # idx-=1
        return cur
    


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        tree=DicTree()
        words=set(words)
        total=0
        nodes=[]
        for word in words:
            nodes.append(tree.insert_reverse(word))
        return sum(len(word)+1 for i,word in enumerate(words) if len(nodes[i].slots)==0)
# @lc code=end
words = ["t"]
assert Solution().minimumLengthEncoding(words)==2

words = ["time", "me", "bell"]
assert Solution().minimumLengthEncoding(words)==10

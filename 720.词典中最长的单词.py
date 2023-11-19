#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#
from typing import List
# @lc code=start
class DictTree:
    def __init__(self) -> None:
        self.slots:dict[str,DictTree]={}
        self.has_word=False
    
    def insert(self,word):
        cur=self
        for ch in word:
            cur=cur.slots.setdefault(ch,DictTree())
        cur.has_word=True
    
    def query_prefix(self,word):
        cur=self
        for ch in word[:-1]:
            cur=cur.slots.get(ch)
            if not cur or cur.has_word==False:
                return False
        return True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # L=len(words)
        # words.sort(key=lambda x:(len(x),x))
        root=DictTree()
        for word in words:
            root.insert(word)
        
        ret=''
        for word in words:
            if root.query_prefix(word):
                if len(word)>len(ret) or(len(word)==len(ret) and word<ret):
                    ret=word
        return ret




# @lc code=end
words=["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]
assert Solution().longestWord(words)=='e'

words=["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
assert Solution().longestWord(words)=='yodn'
words = ["w","wo","wor","worl", "world"]
assert Solution().longestWord(words)=='world'

words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
assert Solution().longestWord(words)=='apple'


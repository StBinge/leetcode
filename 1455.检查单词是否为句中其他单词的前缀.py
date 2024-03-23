#
# @lc app=leetcode.cn id=1455 lang=python3
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
# class Node:
#     def __init__(self) -> None:
#         self.slots={}
#         self.ends=False
#     def insert(self,w:str):
#         cur=self
#         for ch in w:
#             cur=cur.slots.setdefault(ch,Node())
#         cur.ends=True
#     def find()
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,word in enumerate(sentence.split(' '),1):
            if word.startswith(searchWord):
                return i
        return -1
# @lc code=end

assert Solution().isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg")==4
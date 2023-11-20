#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
from typing import List
# @lc code=start
# class Trie:
#     def __init__(self) -> None:
#         self.slots=[None]*26
#         self.word_id=-1
#         # self.suffix=[]
    
#     def add(self,word:str,id:int):
#         cur=self
#         orda=ord('a')
#         # def is_palindrome(left,right):
#         #     while left<right:
#         #         if word[left]!=word[right]:
#         #             return False
#         #         left+=1
#         #         right-=1
#         #     return True
#         N=len(word)
#         for i,ch in enumerate(word):
#             # if is_palindrome(i,N-1):
#             #     cur.suffix.append(id)
#             _ord=ord(ch)-orda
#             if not cur.slots[_ord]:
#                 cur.slots[_ord]=Trie()
#             cur=cur.slots[_ord]
#         cur.word_id=id


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def build_tree(words:list[str]):
            root=[None]*27
            for i,word in enumerate(words):
                cur=root
                for ch in word:
                    idx=ord(ch)-ord('a')
                    if not cur[idx]:
                        cur[idx]=[None]*27
                    cur=cur[idx]
                cur[26]=i
            return root


        reversed_words=[word[::-1] for word in words]
        tree=build_tree(words)
        reversed_tree=build_tree(reversed_words)
        
        def is_palindrome(word:str,left,right):
            while left<right:
                if word[left]!=word[right]:
                    return False
                left+=1
                right-=1
            return True
        
        def match(wid:int,word:str,tree:list,include_eq:bool):
            ret=[]
            if not word:
                return ret
            cur=tree
            L=len(word)
            for i,ch in enumerate(word):
                mid=(i+L)//2

                if cur[26]!=None and is_palindrome(word,i,L-1):
                    ret.append(cur[26])
                cur=cur[ord(ch)-ord('a')]
                if not cur:
                    break
            else:
                if cur[26]!=None and include_eq and cur[26]!=wid:
                    ret.append(cur[26])
            return ret


        
        ret=[]
        
        for i,word in enumerate(words):
            for j in match(i,word,reversed_tree,True):
                ret.append([i,j])
            for j in match(i,word[::-1],tree,False):
                ret.append([j,i])
        return ret

# @lc code=end
words = ["a","abc","aba",""]
res=Solution().palindromePairs(words)
print(res)
assert len(res)==4

words = ["abcd","dcba","lls","s","sssll"]
res=Solution().palindromePairs(words)
print(res)
assert len(res)==4


words = ["bat","tab","cat"]
res=Solution().palindromePairs(words)
print(res)
assert len(res)==2

words = ["a",""]
res=Solution().palindromePairs(words)
print(res)
assert len(res)==2
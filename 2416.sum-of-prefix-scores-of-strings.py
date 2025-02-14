#
# @lc app=leetcode.cn id=2416 lang=python3
# @lcpr version=30204
#
# [2416] 字符串的前缀分数和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.nodes={}
        self.cnt=0
    
    def insert(self,s):
        cur=self
        for ch in s:
            cur=cur.nodes.setdefault(ch,Trie())
            cur.cnt+=1
    
    def query(self,s):
        cur=self
        ret=0
        for ch in s:
            cur=cur.nodes.get(ch,None)
            if not cur:
                break
            ret+=cur.cnt
        return ret
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root=Trie()
        for word in words:
            root.insert(word)
        
        ret=[]
        for word in words:
            ret.append(root.query(word))
        return ret
# @lc code=end



#
# @lcpr case=start
# ["abc","ab","bc","b"]\n
# @lcpr case=end

# @lcpr case=start
# ["abcd"]\n
# @lcpr case=end

#


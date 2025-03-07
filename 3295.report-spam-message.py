#
# @lc app=leetcode.cn id=3295 lang=python3
# @lcpr version=30204
#
# [3295] 举报垃圾信息
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.slots={}
        self.ending=False
    
    def add(self,word):
        cur=self
        for ch in word:
            cur=cur.slots.setdefault(ch,Trie())
        cur.ending=True
    
    def query(self,word):
        cur=self
        for ch in word:
            cur=cur.slots.get(ch,None)
            if not cur:
                return False
        return cur.ending

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        root=Trie()
        for w in bannedWords:
            root.add(w)
        
        cnt=0
        for w in message:
            if root.query(w):
                cnt+=1
                if cnt==2:
                    return True
        return False
# @lc code=end
assert Solution().reportSpam(["mzx","nzc","si","q","bqytc","spp","e"],["qq","em","auju","or","mmiy","g","viu"])==False


#
# @lcpr case=start
# ["hello","world","leetcode"]\n["world","hello"]\n
# @lcpr case=end

# @lcpr case=start
# ["hello","programming","fun"]\n["world","programming","leetcode"]\n
# @lcpr case=end

#


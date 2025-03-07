#
# @lc app=leetcode.cn id=3291 lang=python3
# @lcpr version=30204
#
# [3291] 形成目标字符串需要的最少字符串数 I
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.slots={}
    
    def add(self,word):
        cur=self
        for ch in word:
            cur=cur.slots.setdefault(ch,Trie())
    
    def query(self,word,left,right):
        cur=self
        for ch in word[left:right+1]:
            cur=cur.slots.get(ch,None)
            if not cur:
                return False
        return True

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root=Trie()
        for w in words:
            root.add(w)

        N=len(target)
        f=[float('inf')]*(N+1)
        f[0]=0
        for i in range(N):
            for j in range(i,-1,-1):
                if root.query(target,j,i):
                    f[i+1]=min(f[i+1],f[j]+1)
        return f[-1] if f[-1]<float('inf') else -1


# @lc code=end
assert Solution().minValidStrings(["ea","a"],"eaeaa")==3
assert Solution().minValidStrings(words = ["abcdef"], target = "xyz")==-1
assert Solution().minValidStrings(words = ["abababab","ab"], target = "ababaababa")==2
assert Solution().minValidStrings( words = ["abc","aaaaa","bcdef"], target = "aabcdabc")==3


#
# @lcpr case=start
# ["abc","aaaaa","bcdef"]\n"aabcdabc"\n
# @lcpr case=end

# @lcpr case=start
# ["abababab","ab"]\n"ababaababa"\n
# @lcpr case=end

# @lcpr case=start
# ["abcdef"]\n"xyz"\n
# @lcpr case=end

#


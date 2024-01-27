#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 删除子文件夹
#
from sbw import *
# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.slots={}
        self.end=-1
    
    def add(self,folder:str,i):
        path=folder.split('/')
        cur=self
        for d in path:
            cur=cur.slots.setdefault(d,TrieNode())
        cur.end=i
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root=TrieNode()
        for i,f in enumerate(folder):
            root.add(f,i)
        ret=[]

        def dfs(node:TrieNode):
            if node.end>=0:
                ret.append(folder[node.end])
                return
            for child in node.slots.values():
                dfs(child)
        
        dfs(root)
        return ret
# @lc code=end
assert sorted(Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))==sorted(["/a","/c/d","/c/f"])
assert sorted(Solution().removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))==sorted(["/a/b/c","/a/b/ca","/a/b/d"])
assert sorted(Solution().removeSubfolders( ["/a/b/c","/a/b/ca","/a/b/d"]))==sorted(["/a/b/c","/a/b/ca","/a/b/d"])
assert sorted(Solution().removeSubfolders( ["/a","/a/b/c","/a/b/d"]))==sorted(["/a"])
assert sorted(Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))==sorted(["/a","/c/d","/c/f"])

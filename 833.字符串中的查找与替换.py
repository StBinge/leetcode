#
# @lc app=leetcode.cn id=833 lang=python3
#
# [833] 字符串中的查找与替换
#
from typing import List
# @lc code=start
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n=len(indices)
        ops=sorted(range(n),key=lambda x:indices[x])
        ret=[]
        idx=0
        for op in ops:
            indice=indices[op]
            pat=sources[op]
            tar=targets[op]
            l=len(pat)
            if s[indice:indice+l]==pat:
                ret.append(s[idx:indice])
                ret.append(tar)
                idx=indice+l
        ret.append(s[idx:])
        return ''.join(ret)
# @lc code=end
s = "abcd"
indices = [0,2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
ret="eeecd"
assert Solution().findReplaceString(s,indices,sources,targets)==ret

s = "abcd"
indices = [0,2]
sources = ["a","cd"]
targets = ["eee","ffff"]
ret="eeebffff"
assert Solution().findReplaceString(s,indices,sources,targets)==ret
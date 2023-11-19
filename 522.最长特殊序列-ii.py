#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#
from typing import List
# @lc code=start
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # map={}
        # for i in range(len(strs)):
        #     l=len(strs[i])
        #     ar=map.setdefault(l,[])
        #     ar.append(i)
        
        def has_parent(idx):
            for i in range(len(strs)):
                if i==idx:
                    continue
                l,li=len(strs[idx]),len(strs[i])
                if l>li:
                    return False
                pi=p=0
                s=strs[idx]
                si=strs[i]
                while pi<li and p<l:
                    if s[p]==si[pi]:
                        p+=1
                        pi+=1
                    else:
                        pi+=1
                if p==l:
                    return True
            return False
        strs.sort(key=lambda x:len(x),reverse=True)
        for i in range(len(strs)):
            if not has_parent(i):
                return len(strs[i])
        return -1

        
        
# @lc code=end
strs=["aba","cdc","eae"]
assert Solution().findLUSlength(strs)==3

strs = ["aaa","aaa","aa"]
assert Solution().findLUSlength(strs)==-1

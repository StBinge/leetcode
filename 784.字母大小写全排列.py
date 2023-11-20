#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s=list(s)
        L=len(s)
        ret=[]
        def dfs(s:str,idx):
            nonlocal L
            while idx<L and s[idx].isdigit():
                idx+=1
            if idx==L:
                ret.append(''.join(s))
                return
            s[idx]=s[idx].lower()
            dfs(s,idx+1)
            s[idx]=s[idx].upper()
            dfs(s,idx+1)
        dfs(s,0)
        return ret
# @lc code=end


#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#
from typing import List
# @lc code=start
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ret=[]
        cur=[]
        inblock=False
        for line in source:
            idx=0
            L=len(line)
            while idx<L:
                if inblock:
                    if line[idx]=='*' and idx+1<L and line[idx+1]=='/':
                        inblock=False
                        idx+=1
                elif line[idx]=='/' and idx+1<L:
                    if line[idx+1]=='*':
                        inblock=True
                        idx+=1
                    elif line[idx+1]=='/':
                        break
                    else:
                        cur.append(line[idx])
                else:
                    cur.append(line[idx])
                idx+=1
            if not inblock and len(cur):
                ret.append(''.join(cur))
                cur=[]
            
            
        return ret
# @lc code=end
source=["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
assert Solution().removeComments(source)==[
    "void func(int k) {",
    "   k = k*2/4;",
    "   k = k/2;*/",
    "}"]

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
assert Solution().removeComments(source)==["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

source = ["a/*comment", "line", "more_comment*/b"]
assert Solution().removeComments(source)==['ab']

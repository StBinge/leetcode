#
# @lc app=leetcode.cn id=388 lang=python3
#
# [388] 文件的最长绝对路径
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dep_len=[]
        ret=0
        idx=0
        L=len(input)
        while idx<L:
            depth=0
            length=0
            is_file=False
            while idx<L and input[idx]=='\t':
                depth+=1
                idx+=1
            while idx<L and input[idx]!='\n':
                length+=1
                if input[idx]=='.':
                    is_file=True
                idx+=1
            while len(dep_len)>depth:
                dep_len.pop()
            parent_len=dep_len[-1] if dep_len else 0
            if is_file:
                ret=max(ret,length+parent_len)
            else:
                dep_len.append(length+1+parent_len)
            idx+=1
        return ret
            
# @lc code=end
assert Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")==20
assert Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")==32

assert Solution().lengthLongestPath("a")==0

assert Solution().lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt")==12



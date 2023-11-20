#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        L=len(s)
        def get_string(idx:int):
            nonlocal s,L
            seg=[]
            while idx<L:
                if s[idx].isalpha():
                    seg.append(s[idx])
                    idx+=1
                elif s[idx].isdigit():
                    num=0
                    while s[idx].isdigit():
                        num=num*10+int(s[idx])
                        idx+=1
                    idx+=1
                    idx,ss=get_string(idx)
                    seg.append(ss*num)
                elif s[idx]==']':
                    idx+=1
                    break
            return idx,''.join(seg)
        _,ret= get_string(0)
        return ret
            
# @lc code=end

assert Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")=="zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

assert Solution().decodeString("3[a]2[bc]")=="aaabcbc"
assert Solution().decodeString("3[a2[c]]")=="accaccacc"
assert Solution().decodeString("2[abc]3[cd]ef")=="abcabccdcdcdef"
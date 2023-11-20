#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        si=len(s)-1
        ti=len(t)-1
        def get_valid_idx(s:str,idx):
            if idx<0:
                return idx
            back=0
            while idx>=0 and (back>0 or s[idx]=='#'):
                if s[idx]=='#':
                    back+=1
                else:
                    back-=1
                idx-=1
            return idx

        pass
        while si>=0 or ti >=0:
            si=get_valid_idx(s,si)
            ti=get_valid_idx(t,ti)
            schr=s[si] if si>=0 else ''
            tchr=t[ti] if ti>=0 else ''
            if tchr!=schr:
                return False
            si-=1
            ti-=1
        return True
# @lc code=end
s="bbbextm"
t="bbb#extm"
assert Solution().backspaceCompare(s,t)==False

s = "ab#c"
t = "ad#c"
assert Solution().backspaceCompare(s,t)

s = "ab##"
t = "c#d#"
assert Solution().backspaceCompare(s,t)

s = "a#c"
t = "b"
assert Solution().backspaceCompare(s,t)==False

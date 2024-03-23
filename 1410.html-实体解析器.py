#
# @lc app=leetcode.cn id=1410 lang=python3
#
# [1410] HTML 实体解析器
#

# @lc code=start
class Solution:
    def entityParser(self, text: str) -> str:
        maps={
            '&quot;':'"',
            '&apos;':"'",
            '&amp;':'&',
            '&gt;':'>',
            '&lt;':'<',
            '&frasl;':'/'
        }
        L=len(text)
        idx=0

        ret=[]
        while idx<L:
            if text[idx]!='&':
                ret.append(text[idx])
                idx+=1
                continue
            for code in maps:
                if code==text[idx:idx+len(code)]:
                    ret.append(maps[code])
                    idx+=len(code)
                    break
            else:
                ret.append('&')
                idx+=1

        return ''.join(ret)



# @lc code=end
assert Solution().entityParser("&&&")=="&&&"
assert Solution().entityParser("&&gt;")=="&>"
assert Solution().entityParser("leetcode.com&frasl;problemset&frasl;all")=="leetcode.com/problemset/all"
assert Solution().entityParser("and I quote: &quot;...&quot;")=="and I quote: \"...\""
assert Solution().entityParser(text = "&amp; is an HTML entity but &ambassador; is not.")=="& is an HTML entity but &ambassador; is not."

#
# @lc app=leetcode.cn id=591 lang=python3
#
# [591] 标签验证器
#

# @lc code=start
import re
class Solution:

    def isValid(self, code: str) -> bool:
        # def check_tag(start:int,end:int):   
        #     ret=[-1,-1]
        #     if code[start]!='<' or code[end]!='>':
        #         return ret
        #     start_end=-1
        #     for i in range(start+1,end):
        #         if code[i].isupper():
        #             continue
        #         elif code[start_end]=='>':
        #             start_end=i
        #             break
        #         else:
        #             return ret
        #     else:
        #         return ret
        #     start_tag_len=start_end-start-1
        #     if start_tag_len<1 or start_tag_len>9:
        #         return ret
            
        #     end_start=-1
        #     for i in range(end-1,start,-1):
        #         if code[i].isupper():
        #             continue
        #         elif code[i]=='/' and code[i-1]=='<':
        #             end_start=i-1
        #             break
        #         else:
        #             return ret
        #     else:
        #         return ret
            
        #     end_tag_len=end-end_start-2
        #     if end_tag_len!=start_tag_len or code[start+1:start_end]!=code[end_start+2:end]:
        #         return ret
        #     return [start_end+1,end_start-1]
        
        # return tag name or ''
        # start is '<' or '/' 
        def extract_tag(start:int,end:int):

            for i in range(start+1,end+1):
                if code[i].isupper():
                    continue
                elif code[i]=='>':
                    return code[start+1:i]
                else:
                    return ''
            return ''
        
        # code[start]=='<'
        def check_cdata(start:int,end:int):
            pattern=r'<!\[CDATA\[.*?\]\]>'
            group=re.match(pattern,code[start:end+1])
            if not group:
                return -1
            return group.span()[1]+start

        # def check_content(start,end):
        #     while start<end and code[start]!='<':
        #         start+=1
            

        L=len(code)
        stack=[]
        idx=0
        while idx<L:
            if code[idx]=='<':
                if idx+1==L:
                    return False
                ch=code[idx+1]
                if ch=='/':
                    if not stack:
                        return False
                    end_tag=extract_tag(idx+1,L-1)
                    if not end_tag or len(end_tag)>9 or not stack or stack[-1]!=end_tag:
                        return False
                    else:
                        stack.pop()
                    idx+=len(end_tag)+3
                elif ch=='!':
                    if not stack:
                        return False
                    data_end=check_cdata(idx,L-1)
                    if data_end<0:
                        return False
                    idx=data_end
                else:
                    if idx>0 and not stack:
                        return False
                    start_tag=extract_tag(idx,L-1)
                    if not start_tag or len(start_tag)>9:
                        return False
                    stack.append(start_tag)
                    idx+=len(start_tag)+2
            elif not stack:
                return False
            else:
                idx+=1

        return len(stack)==0
# @lc code=end

assert Solution().isValid("<DIV>This is the first line <![CDATA[<div> <![cdata]> [[]]</div>   ]]>  <DIV> <A>  <![CDATA[<b>]]>  </A>  <A> <C></C></A></DIV>    </DIV>")
assert Solution().isValid("<DIV>This is the first line <![CDATA[<<<<<<<]]></DIV>")
assert Solution().isValid('<DIV>This is the first line <![CDATA[<div>]]></DIV>')
assert Solution().isValid('<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>')
assert not Solution().isValid('<A>  <B> </A>   </B>')
assert not Solution().isValid('<DIV>  div tag is not closed  <DIV>')
assert not Solution().isValid('<DIV>  unmatched <  </DIV>')
assert not Solution().isValid("<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>")
assert not Solution().isValid("<A></A><B></B>")
#
# @lc app=leetcode.cn id=609 lang=python3
#
# [609] 在系统中查找重复文件
#
from typing import List
# @lc code=start
import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map={}
   
        for path in paths:
            dir,*files=path.split(' ')
            for file in files:
                for i in range(L:=len(file)-1,-1,-1):
                    if file[i]=='(':
                        content=file[i+1:L]
                        sames=content_map.setdefault(content,[])
                        sames.append(dir+'/'+file[:i])
                        break
        ret=[]
        for v in content_map.values():
            if len(v)>1:
                ret.append(v)
        return ret
# @lc code=end
paths = ["root/a 1.txt(FB) 2.txt(a)","root/c 3.txt(Ea)","root/c/d 4.txt(b)","root 4.txt(c)"]
res=Solution().findDuplicate(paths)
print(res)
assert len(res)==0

paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
res=Solution().findDuplicate(paths)
print(res)
assert len(res)==2

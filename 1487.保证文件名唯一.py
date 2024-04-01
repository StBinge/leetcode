#
# @lc app=leetcode.cn id=1487 lang=python3
#
# [1487] 保证文件名唯一
#
from sbw import *
# @lc code=start
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ret=[]
        used={}
        for name in names:
            cnt=used.get(name,0)
            if cnt==0:
                ret.append(name)
                used[name]=1
            else:
                while True:
                    suffix=f'{name}({cnt})'
                    if suffix not in used:
                        ret.append(suffix)
                        used[name]+=1
                        used[suffix]=1
                        break
                    cnt+=1
        return ret


# @lc code=end
assert Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"])==["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)(1)"]
assert Solution().getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"])==["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
assert Solution().getFolderNames(["gta","gta(1)","gta","avalon"])==["gta","gta(1)","gta(2)","avalon"]
assert Solution().getFolderNames(names = ["pes","fifa","gta","pes(2019)"])==["pes","fifa","gta","pes(2019)"]

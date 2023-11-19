#
# @lc app=leetcode.cn id=691 lang=python3
#
# [691] 贴纸拼词
#
from typing import List
# @lc code=start
from collections import Counter
# from functools import lru_cache
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # chars_cnt=[Counter(s) for s in stickers]
        for ch in set(target):
            for sticker in stickers:
                if ch in sticker:
                    break
            else:
                return -1
        target_cnt=Counter(target)
        chars_cnt=[]
        for sticker in stickers:
            cnt={}
            for ch in sticker:
                if ch in target_cnt:
                    val=cnt.get(ch,0)+1
                    cnt[ch]=val
            chars_cnt.append(cnt)

        chars_cnt.sort(key=lambda x:sum(x.values()),reverse=True)
        memo={}
        def mask_hash(d:dict):
            ret=0
            for v in d.values():
                ret=ret*10+v
            return ret
        def least_pick(targets:dict):
            hash=mask_hash(targets)
            if hash==0:
                return 0
            if hash in memo:
                return memo[hash]
            
            
            ret=15
            for chars in chars_cnt:
                next_target={key:max(0,targets[key]-chars.get(key,0)) for key in targets}
                next_hash=mask_hash(next_target)
                if next_hash==hash:
                    continue
                ret=min(ret,least_pick(next_target))
            memo[hash]=ret+1
            return memo[hash]
        return least_pick(target_cnt)
# @lc code=end
stickers = ["with","example","science"]
target = "thehat"
assert Solution().minStickers(stickers,target)==3

stickers = ["notice","possible"]
target = "basicbasic"
assert Solution().minStickers(stickers,target)==-1
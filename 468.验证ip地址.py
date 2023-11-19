#
# @lc app=leetcode.cn id=468 lang=python3
#
# [468] 验证IP地址
#

# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        L=len(queryIP)
        Nei='Neither'
        if '.' in queryIP:
            parts=queryIP.split('.')
            if len(parts)!=4:
                return 'Neither'
            for part in parts:
                if not part or (len(part)>1 and part[0]=='0'):
                    return Nei
                num=0
                for d in part:
                    if ord(d)>ord('9'):
                        return Nei
                    num=num*10 +ord(d)-ord('0')
                if num>255:
                    return Nei
            return 'IPv4'
        if ':' in queryIP:
            parts=queryIP.split(':')
            if len(parts)!=8:
                return Nei
            valid=set('0123456789abcdefABCDEF')
            for part in parts:
                if not part or len(part)>4:
                    return Nei
                for ch in part:
                    if ch not in valid:
                        return Nei
            return 'IPv6'
        return Nei
# @lc code=end

assert Solution().validIPAddress("222.2f.22.1")=='Neither'
assert Solution().validIPAddress("172.16.254.1")=='IPv4'
assert Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")=='IPv6'
assert Solution().validIPAddress("256.256.256.256")=='Neither'
assert Solution().validIPAddress("1.0.1.")=='Neither'
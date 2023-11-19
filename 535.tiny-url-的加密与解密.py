#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#

# @lc code=start
class Codec:
    def __init__(self) -> None:
        self.url_id={}
        self.id_url={}
        self.idx=0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.url_id:            
            self.url_id[longUrl]=self.idx
            self.id_url[self.idx]=longUrl
            self.idx+=1
        return 'http://tinyurl.com/'+str(self.url_id[longUrl])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        idx=shortUrl.split('/')[-1]
        return self.id_url[int(idx)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
url = "https://leetcode.com/problems/design-tinyurl"
obj=Codec()
short=obj.encode(url)
print(short)
origin=obj.decode(short)
print(origin)

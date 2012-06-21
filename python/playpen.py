# coding=utf-8
import re
import httplib
import urllib
import base64

#from urlparse import urlparse
#o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html?a=d')
#print o.scheme
#print o.path

def start_xdebug_session(url):
  m = re.match(r"https?://(?P<host>[\w:\.]+)(?P<path>/.*)", url)
  path = m.group('path')
  if path.find('&') == -1:
    path += "?XDEBUG_SESSION_START=1"
  else:
    path += "&XDEBUG_SESSION_START=1"

  conn = httplib.HTTPConnection(m.group('host'))
  conn.request("GET", path)
  r1 = conn.getresponse()
  print r1.status, r1.reason
  print r1.read()

#start_xdebug_session("https://localhost/test.php")
class A:
    def run(self):
        self.help()
    def help(self):
        print "A::help()"

class B(A):
    def run(self):
        self.help()
    def help(self):
        print "B::help()"
a = B()
a.run()

print urllib.quote_plus("https://localhost/test.php")
print urllib.quote_plus("echo 'brook hong is here' > announcements.txt")
print urllib.quote_plus("\\\"")
import cgi
print cgi.escape("<a href='test'>Test</a>", False)

import HTMLParser
htmlparser = HTMLParser.HTMLParser()
print htmlparser.unescape("&gt;")

print base64.encodestring("print 'yes'")
print base64.decodestring("aWYgKCdjbGknID09PSBwaHBfc2FwaV9uYW1lKCkpIHsgcHJpbnQgJ3llcyc7IH0=")

#ret = [[["你好中国","hello chinese people","Nǐ hǎo zhōngguó",""]],,"en",,[["你好",[5],0,0,1000,0,1,0],["中国",[6],0,0,1000,1,2,0]],[["hello",5,[["你好",1000,0,0],["您好",0,0,0],["打招呼",0,0,0],["招呼",0,0,0],["问好",0,0,0]],[[0,5]],"hello chinese people"],["chinese",6,[["中国",1000,0,0],["中国的",0,0,0],["中国人",0,0,0]],[[6,13]],""]],,,[["en"]],10]

ret =[['你好1'],2]
#print u'哈哈'.encode('utf-8')
print ret[0][0]


import asyncore, socket

class http_client(asyncore.dispatcher):

    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, 80) )
        self.buffer = 'GET %s HTTP/1.0\r\n\r\n' % path

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print self.recv(8192)

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

c = http_client('translate.google.com', '/translate_a/t?client=t&text=hello%20chinese%20people&hl=en&sl=en&tl=zh&multires=1&otf=1&ssel=0&tsel=0&sc=1')

asyncore.loop()


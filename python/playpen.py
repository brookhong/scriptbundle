import re
import httplib
import urllib

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


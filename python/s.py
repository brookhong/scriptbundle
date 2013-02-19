# vim: tabstop=2 shiftwidth=2 softtabstop=2 expandtab
import socket,os,time
from threading import Thread,Lock
tracelog = open(os.getenv("HOME").replace("\\","/")+"/.dbgpavim.trace",'w')
def DBGPavimTrace(log):
  tracelog.write("\n"+log+"\n")
  tracelog.flush()

def StopServer():
  global dServer
  if dServer != None:
    dServer.stop()


class DbgSilentClient(Thread):
  def __init__(self, ss):
    self.sock = ss
    Thread.__init__(self)
  def run(self):
    global dServer
    data = self.sock.recv(1024)
    if data:
      DBGPavimTrace('# %s\n' % data)
    if data == "stop":
      dServer.stop()

class DbgListener(Thread):
  (INIT,LISTEN,CLOSED) = (0,1,2)
  def __init__(self, port):
    self.port     = port
    self._status  = self.INIT
    self.lock = Lock()
    Thread.__init__(self)
  def start(self):
    Thread.start(self)
    time.sleep(0.1)
  def stop(self):
    self.lock.acquire()
    try:
      if self._status == self.LISTEN:
        client = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        client.connect ( ( '127.0.0.1', self.port ) )
        client.close()
    finally:
      self._status = self.CLOSED
      self.lock.release()
  def status(self):
    self.lock.acquire()
    s = self._status
    self.lock.release()
    return s
  def run(self):
    self.lock.acquire()
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.settimeout(None)
    try:
      serv.bind(('', self.port))
    except socket.error, e:
      print "Can not bind to port "+str(self.port)+', Socket Error '+str(e[0])
      self.lock.release()
      return
    print ""
    serv.listen(5)
    self._status = self.LISTEN
    self.lock.release()
    while 1:
      (sock, address) = serv.accept()
      DBGPavimTrace('# Connection from %s:%d\n' % (address[0], address[1]))
      s = self.status()
      if s == self.LISTEN:
          client = DbgSilentClient(sock)
          client.start()
      else:
        break
    serv.close()

dServer = DbgListener(5110)
dServer.start()

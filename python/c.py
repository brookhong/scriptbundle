import socket,sys
client = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
client.connect ( ( '127.0.0.1', 5110 ) )
if len(sys.argv) > 1:
  client.send(sys.argv[1])
else:
  client.send("stop")
client.close()

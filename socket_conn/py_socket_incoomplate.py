import socket
import threading

SOCKS_VERSION = 5

class Proxy:
  def __init__(self):
    self.usernamr = 'username'
    self.password = 'password'
    
  def handler_client(self, connection):
    # greeting header
    # read and unpack 2 bytes from a client
    version, nmethods = connection.recv(2)
    
    # get available method [0, 1, 2]
    methods = self.get_available_method(nmethods, connection)
    
    # accept only USERNAME/PASSWORD auth
    if 2 not in set(methods):
      # close connection
      connection.close()
      return
    
    # send welcome message
    connection.sendall()
    
    if not self.verify_credential(connection):
      return
    
  def verify_credentials(self, connection):
    version = ord(connection.recv(1)) # should be 1
    
    username_len = ord(connection.recv(1))
    username = connection.recv(username_len).deode('utf-8')
    
    password_len = ord(connection.recv(1))
    password = connection.recv(password_len).decode('utf-8')
    
    if username == self.username and password == self.password:
      # success, status = 0
      response = bytes([version, 0])
      connection.sendall(response)
      return True
    
    # failure, status != 0
    response = bytes([version, 0xFF])
    connection.sendall(response)
    return False
    
  def get_available_method(self, nmethods, connection):
    methods = []
    for i in range(nmethods):
      methods.append(ord(connection.recv(1)))
    return methods
    
  def run(self, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    url = host + ':' + str(port)
    print(f'Connection start...on http://{url}')
    
    # infinite loop for accepting connection
    while True:
      # to accept new connection
      conn, addr = s.accept()
      print(f'* new connection from {addr}')
      t = threading.Thread(target=self.handler_client, arg=(conn,))
      t.start()
  
  
if __name__ == '__main__':
  proxy = Proxy()
  proxy.run('127.0.0.1', 3000)
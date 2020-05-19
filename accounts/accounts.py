# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))

import socketserver
from pyparsing.parsing import PyParsing

class AccountRequestProcessor(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        #print("{} wrote:".format(self.client_address[0]))
        data_as_string = self.data.decode("utf-8")
        callback, token, data = PyParsing.parseMessageFromClient(data_as_string)
        # just send back the same data, but upper-cased
        if token != None:
            print(str(data))
            self.request.sendall("{response: 'test'}".encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), AccountRequestProcessor)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
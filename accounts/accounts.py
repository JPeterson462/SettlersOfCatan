import socketserver
import re
import urllib
import urllib.parse

class AccountRequestProcessor(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        filter = 'GET \/\?([^ ]+)'
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        #print("{} wrote:".format(self.client_address[0]))
        m = re.search(filter, self.data.decode("utf-8"))
        if m:
            found = m.group(1)
            content = urllib.parse.parse_qs(found)
            callback = content['callback'][0]
            token = content['_'][0]
            data = dict()
            for key, value in content.items():
                layers = key.replace("]", "").split("[")
                if layers[0] != "callback" and layers[0] != "_":
                    current = data
                    for layer in layers:
                        if not layer in current.keys():
                            current[layer] = dict()
                        current = current[layer]
                    current = data
                    i = 0
                    while i < len(layers) - 1:
                        current = current[layers[i]]
                        i += 1
                    current[layers[i]] = value
            print("Callback: " + callback)
            print("Token: " + token)
            print("Data: " + str(data))
            print(content)
            # just send back the same data, but upper-cased
            self.request.sendall("{response: 'test'}".encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), AccountRequestProcessor)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
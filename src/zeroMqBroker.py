__author__ = 'matt'

import zmq

class ZeroMQBroker:
    LISTEN_PORT = "5556"

    def __init__(self):
        # Socket to talk to server
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect("tcp://localhost:%s" % self.LISTEN_PORT)

    def startMessageListener(self, partyID):
        self.socket.setsockopt(zmq.SUBSCRIBE, partyID)

        while True:
            message = self.socket.recv_string()
            messageParts = message.split()
            topic = messageParts[0]
            verb = messageParts[1]
            argument = None

            if len(messageParts) > 2:
                argument = messageParts[2]

            if verb == "loadPlaylist":
                print argument

if __name__ == "__main__":
    test = ZeroMQBroker()
    test.startMessageListener("house1")
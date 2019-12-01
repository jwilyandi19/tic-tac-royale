import server.app.server as serverMod
import Pyro4

class TicTacToeServer:
    def __init__(self, host, port, identifier="main-"):
        self.server = serverMod.Server(host, port, identifier)

    def Start(self):
        self.server.Start([self])


server = TicTacToeServer("localhost", 7777)
server.Start()
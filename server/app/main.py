import server.app.server as serverMod
import server.app.tictacservice as tttService
import Pyro4

class TicTacToeServer:
    def __init__(self, host, port, identifier="main-"):
        self.server = serverMod.Server(host, port, identifier)
        self.tttService = tttService.TicTacService()
    
    def Start(self):
        self.server.Start([self])

    def Create(self):
        try:
            room = self.tttService.Create()
            return {
                "data": room
            }
        except Exception as e:
            return self.handleError(e)
    
    def Join(self,code):
        try:
            self.tttService.Join(code)
        except Exception as e:
            return self.handleError(e)
    
    def ListByRoom(self,code):
        try:
            pawns = self.tttService.ListByRoom(code)
            return {
                "data": pawns
            }
        except Exception as e:
            return self.handleError(e)
    
    def Place(self,x_coord,y_coord,code):
        try:
            self.tttService.Place(x_coord,y_coord,code)
        except Exception as e:
            return self.handleError(e)
    
    def handleError(self, err):
        return {
            "error": str(err)
        }


server = TicTacToeServer("localhost", 7777)
server.Start()
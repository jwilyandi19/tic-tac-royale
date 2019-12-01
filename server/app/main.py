import server.app.server as serverMod
import server.app.tictacservice as tttService
import Pyro4
import json

class TicTacToeServer:
    def __init__(self, host, port, identifier="main-"):
        self.server = serverMod.Server(host, port, identifier)
        self.tttService = tttService.TicTacService()
    
    def Start(self):
        self.server.Start([self])

    def Create(self):
        try:
            response = self.tttService.Create()
            return {
                "data": response
            }
        except Exception as e:
            return self.handleError(e)
    
    def Join(self,code):
        try:
            response = self.tttService.Join(code)
            return {
                "data": response
            }
        except Exception as e:
            return self.handleError(e)
    
    def ListByRoom(self,code):
        try:
            response = self.tttService.ListByRoom(code)
            return {
                "data": response
            }
        except Exception as e:
            return self.handleError(e)
    
    def Place(self,x_coord,y_coord,code):
        try:
            response = self.tttService.Place(x_coord,y_coord,code)
            return {
                "data": response
            }
        except Exception as e:
            return self.handleError(e)
    
    def handleError(self, err):
        return {
            "error": str(err)
        }


server = TicTacToeServer("localhost", 7777)
server.Start()
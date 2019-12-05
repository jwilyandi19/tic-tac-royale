import tkinter as tki
import client.frame.home as fHomeMod
import client.frame.create_room as fCreateRoomMod
import client.frame.join_room as fJoinRoomMod
import client.asset.font as fontMod
import client.frame.stack as stackMod
import client.client as clientMod
import client.frame.board_player as fBoardPlayer


class TicTacToeClient:

    def __init__(self, host, port, identifier="main-"):
        self.client = clientMod.Client(host, port, identifier)
        self.client.Start(["TicTacToeServer"])
        self.server = self.client.GetObject("TicTacToeServer")
    
    def Create(self):
        response = self.server.Create()
        return response
    
    def Join(self,code):
        response = self.server.Join(code)
        return response
    
    def ListByRoom(self,code):
        response = self.server.ListByRoom(code)
        return response
    
    def Place(self,x_coord,y_coord,code):
        response = self.server.Place(x_coord,y_coord,code)
        return response

def RunGUI():
    root = tki.Tk()
    fontMod.Font.Initialize(root)
    root.title("Tic Tac Royale")
    root.resizable(width=False, height=False)
    stackFrame = stackMod.FrameStack(root)
    home = fHomeMod.Home(stackFrame)
    fCreateRoomMod.CreateRoom(stackFrame)
    fJoinRoomMod.JoinRoom(stackFrame)
    fBoardPlayer.BoardPlayer(stackFrame)
    stackFrame.push(home)
    root.mainloop()

RunGUI()
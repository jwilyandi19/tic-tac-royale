import server.domain.usecase.create_room as createRoomUC
import server.domain.usecase.join_room as joinRoomUC
import server.domain.usecase.list_pawn_by_room as listPawnByRoomUC
import server.domain.usecase.place_pawn as placePawnUC



class TicTacService():

    def __init__(self,create_room: createRoomUC.CreateRoom, 
    join_room: joinRoomUC.JoinRoom, list_pawn_by_room: listPawnByRoomUC.ListPawnByRoom, 
    place_pawn: placePawnUC.PlacePawn):
        self.create_room = create_room
        self.join_room = join_room
        self.list_pawn_by_room = list_pawn_by_room
        self.place_pawn = place_pawn
    
    def Create(self):
        room = self.create_room.Create()
        return room
    
    def Join(self, code):
        self.join_room.Join(code)
        return "OK"
    
    def ListByRoom(self,code):
        pawns = self.list_pawn_by_room.ListByRoom(code)
        return pawns
    
    def Place(self,x_coord,y_coord,code):
        self.place_pawn.Place(x_coord,y_coord,code)
        return "OK"
    



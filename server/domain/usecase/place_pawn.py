import server.domain.model.pawn as pawnMod
import server.domain.model.location as locMod
import server.domain.model.room as roomMod
import server.domain.model.tictactoe as tictactoeMod

class PlacePawn:
    def execute(self,x_coord,y_coord,code):
        location = locMod.Location(x_coord,y_coord)
        room = roomMod.Room(code)
        pawn_type = room.getAvailableSpot()

        pawn = pawnMod.Pawn(pawn_type,location)

        if(not tictactoeMod.TicTacRoyale.hasPawn(location)):
            room.addPawn(pawn)
        else:
            raise Exception("Pawn has been placed")
        




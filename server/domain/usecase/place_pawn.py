import server.domain.model.pawn as pawnMod
import server.domain.model.location as locMod

class PlacePawn:
    def execute(self,x_coord,y_coord,turn):
        pawn_type = ""
        location = locMod.Location(x_coord,y_coord)
        if turn == 0:
            pawn_type = pawnMod.PawnType.X
        else:
            pawn_type = pawnMod.PawnType.O
        
        pawnMod.Pawn(pawn_type,location)


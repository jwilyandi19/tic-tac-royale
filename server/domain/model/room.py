import server.domain.model.pawn as pawnMod
import typing as typ

class Room:
    def __init__(self, code: str):
        self.code = code
        self.availableSpot = [pawnMod.PawnType.X, pawnMod.PawnType.O]
        self.pawns = typ.Sequence[pawnMod.Pawn]()

    def addPawn(self, pawn: pawnMod.Pawn):
        self.pawns.append(pawn)

    def getCode(self) -> str:
        return self.code

    def getAvailableSpot(self) -> pawnMod.PawnType:
        size = self.availableSpot.count()
        if size > 0:
            return self.availableSpot.pop()
        return None
            
    def addAvailableSpot(self, pawn: pawnMod.PawnType):
        self.availableSpot.append(pawn)

    def isPawnAvailable(self, pawn: pawnMod.PawnType) -> bool:
        return pawn in self.availableSpot

    def getPawns(self) -> typ.Sequence[pawnMod.Pawn]:
        return self.pawns
import server.domain.model.room as roomMod
import server.domain.model.location as locMod
import server.domain.model.pawn as pawnMod

import typing as typ

class TicTacRoyale:
    
    def __init__(self):
        self.pawnMap = typ.Dict[locMod.Location, pawnMod.Pawn]()
        self.rooms = typ.Dict[str, roomMod.Room]()

    def createRoom(self) -> roomMod.Room:
        raise Exception("Not Implemented")

    def hasPawn(self, location: locMod.Location) -> bool:
        return location in self.pawnMap

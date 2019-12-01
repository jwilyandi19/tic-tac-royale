import server.domain.model.pawn as pawnMod
import server.domain.model.location as locMod
import server.domain.model.room as roomMod
import server.domain.model.tictactoe as tttMod
import asyncio.locks as lockMod


class PlacePawn:
    def __init__(self, ticTacToe: tttMod.TicTacRoyale, lock: lockMod.Lock):
        self.tictactoe = ticTacToe
        self.lock = lock

    def execute(self,x_coord,y_coord,code):
        location = locMod.Location(x_coord,y_coord)
        room = tictactoe.findRoom(code)
        pawn_type = room.getAvailableSpot()
        self.lock.acquire()
        pawn = pawnMod.Pawn(pawn_type,location)
        tictactoe.addPawn(pawn)
        self.lock.release()
        




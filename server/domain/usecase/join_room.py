import server.domain.model.tictactoe as tttMod
import server.domain.model.room as roomMod
import asyncio.locks as lockMod

class JoinRoom():

    def __init__(self, ticTacToe: tttMod.TicTacRoyale, lock: lockMod.Lock):
        self.tictactoe = ticTacToe
        self.lock = lock

    def execute(self, code):
        self.lock.acquire()
        room = self.tictactoe.findRoom(code)
        pawn_type = room.getAvailableSpot()

        self.lock.release()


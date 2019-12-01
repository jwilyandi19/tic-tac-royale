import server.domain.model.tictactoe as tttMod
import server.domain.model.room as roomMod
import asyncio.locks as lockMod

class CreateRoom:

    def __init__(self, ticTacToe: tttMod.TicTacRoyale, lock: lockMod.Lock):
        self.tictactoe = ticTacToe
        self.lock = lock

    def execute(self) -> roomMod.Room:
        self.lock.acquire()
        room = self.tictactoe.createRoom()
        self.lock.release()
        return room


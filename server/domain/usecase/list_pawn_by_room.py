import server.domain.model.room as roomMod
import server.domain.model.pawn as pawnMod
import server.domain.model.tictactoe as tttMod

import typing as typ

class ListPawnByRoom:

    def __init__(self, ticTacToe: tttMod.TicTacRoyale):
        self.tictactoe = ticTacToe

    def execute(self,code) -> typ.Sequence[pawnMod.Pawn]:
        room = self.tictactoe.findRoom(code)
        pawns = room.Room.getPawns()

        return pawns
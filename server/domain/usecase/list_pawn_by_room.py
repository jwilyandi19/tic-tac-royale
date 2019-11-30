import server.domain.model.room as roomMod
import server.domain.model.pawn as pawnMod

import typing as typ

class ListPawnByRoom:
    def execute(self,code) -> typ.Sequence[pawnMod.Pawn]:
        code =
        pawns = roomMod.Room.getPawns()

        return pawns
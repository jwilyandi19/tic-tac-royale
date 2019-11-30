import server.domain.model.room as roomMod

class ListPawn:
    def execute(self):
        pawns = roomMod.Room.getPawns()

        return pawns
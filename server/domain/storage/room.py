import server.domain.model.room as roomMod

class IRoomStorage:

    def getRoom(self, code: int) -> roomMod.Room:
        raise NotImplementedError()

    def setRoom(self, room: roomMod.Room):
        raise NotImplementedError()
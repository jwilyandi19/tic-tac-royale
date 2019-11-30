import server.domain.model.room as roomMod
import server.domain.model.location as locMod
import server.domain.model.pawn as pawnMod

import server.domain.storage.pawn as pawnStorMod
import server.domain.storage.room as roomStorMod

import typing as typ
import random

class TicTacRoyale:
    
    def __init__(self, pawnStorage: pawnStorMod.IPawnStorage, roomStorage: roomStorMod.IRoomStorage):
        self.pawns = pawnStorage
        self.rooms = roomStorage

    def createRoom(self) -> roomMod.Room:
        code = random.randint(0, 10000000)
        while findRoom(code) is not None:
            code = random.randint(0, 10000000)
        room = roomMod.Room(code)
        self.rooms.setRoom(room)
        return room

    def findRoom(self, code: int) -> roomMod.Room:
        return self.rooms.getRoom(code)

    def hasPawn(self, location: locMod.Location) -> bool:
        return self.getPawn(location) is not None

    def getPawn(self, location: locMod.Location) -> pawnMod.Pawn:
        return self.pawns.getPawn(self.pawns)

    def addPawn(self, pawn: pawnMod.Pawn):
        if self.hasPawn(pawn.getLocation()):
            raise Exception("Location already used")
        self.addPawn(pawn)


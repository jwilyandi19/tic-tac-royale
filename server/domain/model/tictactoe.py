import server.domain.model.room as roomMod
import server.domain.model.location as locMod
import server.domain.model.pawn as pawnMod
import server.domain.model.placement as placMod

import server.domain.storage.pawn as pawnStorMod
import server.domain.storage.room as roomStorMod
import server.domain.storage.placement as placStorMod

import typing as typ
import random

class TicTacRoyale:
    
    def __init__(self, placementStorage: placStorMod.IPlacementStorage, roomStorage: roomStorMod.IRoomStorage):
        self.rooms = roomStorage
        self.placements = placementStorage

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
        return self.getPlacement(location) is not None

    def getPlacement(self, location: locMod.Location) -> pawnMod.Pawn:
        return self.placements.getPlacement(location)

    def addPawn(self,room: roomMod.Room, pawn: pawnMod.Pawn) -> placMod.Placement:
        if not self.hasPawn(pawn.getLocation()):
            placement = placMod.Placement(room, pawn)
            self.placements.setPlacement(pawn.getLocation(), placement)
            return placement
        else:
            raise Exception("Location already used")
        

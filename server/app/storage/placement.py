import server.domain.storage.placement as placStorMod
import server.domain.model.location as locMod
import server.domain.model.placement as placMod
import typing as typ

class PlacementStorag(placStorMod.IPlacementStorage):

    def __init__(self):
        self.map : typ.Dict[locMod.Location, placMod.Placement] = dict()

    def getPlacement(self, location: locMod.Location) -> placeMod.Placement:
        if location in self.map:
            return self.map[location]
        return None

    def setPlacement(self, location: locMod.Location, placement: placeMod.Placement):
        self.map[location] = placement
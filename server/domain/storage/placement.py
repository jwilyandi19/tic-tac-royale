import server.domain.model.location as locMod
import server.domain.model.placement as placeMod

class IPlacementStorage:
    def getPlacement(self, location: locMod.Location) -> placeMod.Placement:
        raise NotImplementedError()

    def setPlacement(self, location: locMod.Location, placement: placeMod.Placement):
        raise NotImplementedError()
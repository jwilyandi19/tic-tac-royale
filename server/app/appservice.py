import typing as typ

class TicTacService():


    def __init__(self, obj):
        self.map = typ.Dict[str,obj]()

    
    def addService(self,obj):
        self.map[obj.__class__.__name__] = obj


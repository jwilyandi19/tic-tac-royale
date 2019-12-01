import Pyro4
import os
import json
import base64

class Client:
    def __init__(self, host, port, identifier = "main-"):
        self.host = host
        self.port = port
        self.identifier = identifier
        self.objects = dict()

    def Start(self, remoteObjects):
        for obj in remoteObjects:
            url = "PYRONAME:%s%s@%s:%d" % (self.identifier, obj, self.host, self.port)
            self.objects[obj] = Pyro4.Proxy(url)

    def GetObject(self, name):
        return self.objects[name]
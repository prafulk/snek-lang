import socket as sck


class Pipe():
    def __init__(self, name, event):
        self.name = name
        self.event = event
        self._sock = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

        

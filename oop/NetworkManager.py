from Message import *
from dataclasses import dataclass

@dataclass
class NetworkManager:
    status: str

    def process(self, mesg):
        self.status = "processing..."
        reply = Message("photo for: " + mesg.msg)
        self.send(reply)
        self.status = "done"

    def send(self, rep):
        self.status = "sending...."
        print(rep.msg)
        self.status = "sent"

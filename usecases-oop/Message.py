from dataclasses import dataclass

@dataclass
class Message:
    msg: str = ""
    def getMsg(self):
        return self.msg

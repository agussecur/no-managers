from dataclasses import dataclass

@dataclass
class Message:
    txt: str

@dataclass
class PhotoRequest:
    msg: Message

@dataclass
class PhotoReply:
    msg: str

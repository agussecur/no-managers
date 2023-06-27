from Message import *
import unittest

def process(msg: Message) -> str:
    return processPhoto(PhotoRequest(msg)).msg

def processPhoto(req: PhotoRequest) -> PhotoReply:
    return PhotoReply("photo for: " + req.msg.txt)


if __name__ == '__main__':
    class Testing(unittest.TestCase):
        def test_messageReturnsPhotoForClient(self):
            self.assertEqual(process(Message("client")), "photo for: client")

        def test_photoRequestReturnsPhotoReply(self):
            self.assertEqual(processPhoto(PhotoRequest(Message("client"))), PhotoReply("photo for: client"))

    unittest.main()

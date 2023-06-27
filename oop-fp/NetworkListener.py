from Message import *
import unittest

class NetworkListener:
    def __init__(self, msgProcessor, sender):
        self.process = msgProcessor
        self.sender = sender

    def onMessage(self, msg):
        self.sender(self.process(msg))


if __name__ == '__main__':
    class Testing(unittest.TestCase):
        def test_messages_are_processed(self):
            rep = ""
            def sent(msg):
                nonlocal rep
                rep = "message from: " + msg
            sut = NetworkListener(lambda x: x.txt, sent)
            sut.onMessage(Message("client"))
            self.assertEqual(rep, "message from: client")

    unittest.main()

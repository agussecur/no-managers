from Message import *
import unittest

def onMessage(process, send, msg):
    send(process(msg))

if __name__ == '__main__':
    class Testing(unittest.TestCase):
        def test_messages_are_processed(self):
            rep = ""
            def sent(msg):
                nonlocal rep
                rep = "message from: " + msg
            onMessage(lambda x: x.txt, sent, Message("client"))
            self.assertEqual(rep, "message from: client")

    unittest.main()

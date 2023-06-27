class NetworkListener:
    def __init__(self, nwManager):
        self.nwManager = nwManager

    def onMessage(self, msg):
        self.nwManager.process(msg)


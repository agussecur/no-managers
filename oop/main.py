from Message import *
from NetworkListener import *
from NetworkManager import *

print("OOP version")

nl = NetworkListener(NetworkManager())
nl.onMessage(Message("giveme photo"))

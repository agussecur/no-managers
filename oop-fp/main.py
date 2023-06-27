from Message import *
from NetworkListener import *
from ProcessMessage import *

print("FP version")

nl = NetworkListener(process, print)
nl.onMessage(Message("giveme photo"))

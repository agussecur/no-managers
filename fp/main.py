from Message import *
from NetworkListener import onMessage
from ProcessMessage import process
from functools import partial
from pipe import *

apply = Pipe(lambda x, func: func(x))

print("FP version")

def printStatus(x, y):
    print(x)
    return y

def processWithStatus(msg):
    done = partial(printStatus, "done")
    processing = partial(printStatus, "processing") 
    return msg | apply(processing) | apply(process) | apply(done)

onMsg = partial(onMessage, processWithStatus, print)
onMsg(Message("giveme photo"))

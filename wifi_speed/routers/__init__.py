from .base import *
from .hg630_v2 import *

def find_router(name):
    name = name.lower().strip().replace(" ", "_")
    
    if name == "hg630_v2":
        return HG630_v2()

    raise "Not found"
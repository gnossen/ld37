from senator import *
import random

def test_name():
    random.seed()
    for i in range(10):
        senator = Senator()
        print senator.full_name()
        print senator.characteristics

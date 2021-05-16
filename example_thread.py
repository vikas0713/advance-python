"""Understanding thread module of python fro python cook book"""

from threading import Thread
from time import sleep


def countdown(n, thread=False):
    while n > 1:
        if thread:
            print("From Thread running")
        else:
            print("Plain call")
        n -= 1
        sleep(2)


thread1 = Thread(target=countdown, args=(100, True))
thread1.start()
countdown(100)

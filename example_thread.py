"""Understanding thread module of python fro python cook book"""

from threading import Thread
from time import sleep


def countdown(n):
    while n > 1:
        print("running")
        n -= 1
        sleep(5)


countdown(100)

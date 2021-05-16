import threading
from time import sleep


def countdown(n, thread=False):
    while n > 1:
        if not thread:
            print("calling from method")
        else:
            print("calling from thread..........")
        n -= 1
        sleep(2)


thread1 = threading.Thread(target=countdown, args=(100, True), daemon=True)
# thread1.start()
# countdown(n=100)
print(threading.active_count())
print(threading.current_thread())

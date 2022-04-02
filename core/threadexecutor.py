import threading
from functools import partial


def try_forever(f):
    while True:
        try:
            f()
        except:
            print("ERROR")


def wrap_try_forever(f):
    return partial(try_forever, f)


def spin(action, thread_count=0):
    threads = []

    for i in range(thread_count):
        t = threading.Thread(target=wrap_try_forever(action))
        t.daemon = True
        threads.append(t)

    for i in range(thread_count):
        threads[i].start()

    for i in range(thread_count):
        threads[i].join()

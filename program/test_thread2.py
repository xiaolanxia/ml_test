import threading
import time


class MyThread(threading.Thread):

    def __init__(self, id):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(5)
        print("This is %s" % (self.getName()))
if __name__ == '__main__':
    t1=MyThread(999)
    t1.setDaemon(True)
    t1.start()
    print("I am the father thread.")

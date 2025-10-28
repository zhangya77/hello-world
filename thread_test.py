import threading
import time

def print_numbers():
    cur_thread = threading.current_thread()
    tname = cur_thread.name
    tid = cur_thread.ident
    for i in range(5):
        time.sleep(1)
        print(f"tid:{tid} tname:{tname} i:{i}")


thread = threading.Thread(target=print_numbers,name="Thread-0")
thread1 = threading.Thread(target=print_numbers,name="Thread-1")
thread.start()
thread1.start()
thread.join()
thread1.join()
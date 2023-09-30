import multiprocessing
import time
from datetime import datetime
import random

def print_current_time():
    wait_time = random.random()  # Returns a number between 0 and 1
    time.sleep(wait_time)
    print(datetime.now())

if __name__ == "__main__":
    processes = []
    
    for _ in range(3):
        p = multiprocessing.Process(target=print_current_time)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

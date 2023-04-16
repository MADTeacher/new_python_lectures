import random
import threading
import time

counter = 0


def thread_job():
    global counter
    time.sleep(random.randint(0, 1))
    counter += 1
    # old_counter = counter
    # time.sleep(random.randint(0, 1))
    # counter = old_counter + 1



if __name__ == '__main__':
    threads = [threading.Thread(target=thread_job) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(counter) # 10

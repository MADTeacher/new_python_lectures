from multiprocessing import Process, Lock, Value
import time

def increment_counter(lock: Lock, counter: Value) -> None:
    with lock:
        counter.value += 1
        print(f"Counter incremented: {counter.value}")
        time.sleep(1)

if __name__ == "__main__":
    lock = Lock()
    counter = Value('i', 0)
    processes = [
        Process(
            target=increment_counter, 
            args=(lock, counter)
        ) for _ in range(5)
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

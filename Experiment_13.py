"""
Experiment 13 - Multithreading (CO-5)
Create multiple threads to perform different tasks concurrently.
"""
import threading
import time


def print_numbers():
    for i in range(1, 6):
        print(f"[Numbers] {i}")
        time.sleep(0.5)


def print_letters():
    for ch in "ABCDE":
        print(f"[Letters] {ch}")
        time.sleep(0.7)


def calculate_squares(nums):
    for n in nums:
        print(f"[Squares] {n}^2 = {n * n}")
        time.sleep(0.6)


# Shared counter protected with a Lock
counter = 0
lock = threading.Lock()


def increment(times):
    global counter
    for _ in range(times):
        with lock:
            counter += 1


if __name__ == "__main__":
    start = time.time()

    t1 = threading.Thread(target=print_numbers, name="NumberThread")
    t2 = threading.Thread(target=print_letters, name="LetterThread")
    t3 = threading.Thread(target=calculate_squares, args=([2, 3, 4, 5],), name="SquareThread")

    for t in (t1, t2, t3):
        t.start()
    for t in (t1, t2, t3):
        t.join()

    print(f"\nAll tasks finished in {time.time() - start:.2f} seconds")

    # Synchronization demo
    workers = [threading.Thread(target=increment, args=(10000,)) for _ in range(4)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    print("Final counter value (expected 40000):", counter)

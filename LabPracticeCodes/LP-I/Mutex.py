import threading
import time

# Constants
BUFFER_SIZE = 10  # Size of the shared buffer
NUM_ITEMS = 20  # Number of items to produce and consume

# Shared buffer and synchronization primitives
buffer = []
mutex = threading.Lock()  # Mutex for critical section
empty_slots = threading.Semaphore(BUFFER_SIZE)  # Semaphore for empty slots
filled_slots = threading.Semaphore(0)  # Semaphore for filled slots 
    
# Producer function
def producer():
    for item in range(1, NUM_ITEMS + 1):  # Produce items from 1 to 20
        empty_slots.acquire()  # Wait for an empty slot
        mutex.acquire()  # Enter critical section

        # Add item to the buffer
        buffer.append(item)
        print(f"Produced: {item}")

        mutex.release()  # Exit critical section
        filled_slots.release()  # Signal that a new item is available
        # time.sleep(0.5)  # Sleep for a short time to simulate production time

# Consumer function
def consumer():
    for _ in range(NUM_ITEMS):  # Consume 20 items
        filled_slots.acquire()  # Wait for a filled slot
        mutex.acquire()  # Enter critical section

        # Remove item from the buffer
        item = buffer.pop(0)
        print(f"Consumed: {item}")

        mutex.release()  # Exit critical section
        empty_slots.release()  # Signal that an empty slot is available
        # time.sleep(1)  # Sleep for a short time to simulate consumption time

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()
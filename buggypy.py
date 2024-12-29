import os
import threading
import time
import random
import sys
import gc
import multiprocessing
from memory_profiler import profile  # Import memory profiler

# Enable garbage collection debugging
gc.set_debug(gc.DEBUG_LEAK)

def memory_leak():
    """Simulate a memory leak by continuously allocating memory."""
    print("Starting memory leak simulation...")
    leaked_list = []  # This list will hold references to strings.
    
    # Simulate a memory leak by appending large objects to the list.
    while True:
        leaked_list.append('Memory leak' * 1000000)  # Create large string objects.
        print(f"Leaked {len(leaked_list)} objects to memory.")  # Output how many objects we've leaked.
        time.sleep(0.1)  # Sleep for 0.1 seconds to slow down the leak.
        gc.collect()

@profile
def blocked_threads():
    """Simulate blocked threads where multiple threads wait for a long task to complete."""
    print("Starting blocked threads simulation...")
    
    # This worker function simulates a thread that waits for a long task to finish.
    def worker():
        print("Thread started, performing a long task.")
        time.sleep(10)  # Simulate a long-running task by sleeping for 10 seconds.
        print("Thread finished the task.")

    threads = [threading.Thread(target=worker) for _ in range(5)]  # Create 5 threads.
    
    # Start all threads.
    for thread in threads:
        thread.start()

    # Wait for a while to simulate that all threads are blocked and doing nothing.
    time.sleep(1)
    print("All threads are blocked! All threads are waiting for resources.")
    
    # Join all threads (wait for them to finish).
    for thread in threads:
        thread.join()
    print("All threads have finished.")

@profile
def thread_leak():
    """Simulate a thread leak by continuously creating threads that never terminate."""
    print("Starting thread leak simulation...")
    
    # This worker function represents a thread that never terminates.
    def worker():
        while True:
            time.sleep(1)  # Sleep indefinitely, causing the thread to do nothing but consume resources.
    
    # Continuously create and start new threads without ever joining or terminating them.
    while True:
        threading.Thread(target=worker).start()  # Create and start a new thread.
        print("Started a new thread. Thread leak ongoing.")
        time.sleep(0.1)  # Sleep for a short duration before starting another thread.

@profile
def infinite_loop():
    """Simulate an infinite loop that consumes CPU resources."""
    print("Starting infinite loop simulation...")
    
    # This infinite loop will keep the CPU busy and unresponsive.
    while True:
        pass  # Empty loop, consumes CPU time.

@profile
def cpu_stress():
    """Simulate CPU stress by launching multiple processes to stress all CPU cores."""
    print("Starting CPU stress simulation...")

    def stress_cpu():
        """Infinite loop to keep a CPU core busy."""
        while True:
            pass  # This is a busy wait, which keeps the CPU active.

    # Get the number of CPU cores available.
    num_cores = multiprocessing.cpu_count()
    print(f"Detected {num_cores} CPU cores.")
    
    # Create a pool of processes that will each stress a single core.
    processes = []
    for i in range(num_cores):
        p = multiprocessing.Process(target=stress_cpu)
        
        # Optionally set the CPU affinity (if available) to ensure each process runs on a different core.
        if sys.platform != 'win32':  # Setting affinity is not supported on Windows
            p.start()
            p.cpu_affinity([i])  # Affinity to the i-th CPU core
        
        processes.append(p)

    # Start all the processes.
    for p in processes:
        p.start()

    # Wait for the processes to complete (they never will, because of the infinite loops).
    for p in processes:
        p.join()

@profile
def file_descriptor_leak():
    """Simulate a file descriptor leak by continuously opening files without closing them."""
    print("Starting file descriptor leak simulation...")
    
    # This will continually open files without closing them, causing a file descriptor leak.
    while True:
        try:
            open('/dev/null', 'r')  # Open a file descriptor (won't use the file, just leak the resource).
            print("Opened a new file descriptor. File descriptor leak ongoing.")
        except Exception as e:
            print(f"An error occurred while opening a file: {e}")
        time.sleep(0.1)  # Sleep for a short period before opening the next file descriptor.

@profile
def unhandled_exception():
    """Simulate an unhandled exception occurring within a thread."""
    print("Starting unhandled exception simulation...")
    
    # This function will cause a division by zero error in a separate thread.
    def cause_exception():
        print("Thread started. Cause exception now...")
        return 1 / 0  # Division by zero will cause an exception.

    # Start a new thread that will raise an exception.
    thread = threading.Thread(target=cause_exception)
    thread.start()
    
    # Wait for the thread to finish, but it will raise an exception that is not handled.
    thread.join()

@profile
def deadlock():
    """Simulate a deadlock condition where two threads block each other forever."""
    print("Starting deadlock simulation...")
    
    lock1 = threading.Lock()  # Lock 1 will be acquired by the first thread.
    lock2 = threading.Lock()  # Lock 2 will be acquired by the second thread.

    # Thread 1 tries to acquire lock1 and then lock2, while thread 2 tries the opposite.
    def task1():
        with lock1:  # Lock 1 is acquired.
            print("Task 1: Acquired lock1, now waiting for lock2.")
            time.sleep(1)  # Sleep to simulate work before trying for lock2.
            with lock2:  # Lock 2 is acquired here (which task2 already holds).
                print("Task 1: Acquired lock2, completing task.")
    
    def task2():
        with lock2:  # Lock 2 is acquired.
            print("Task 2: Acquired lock2, now waiting for lock1.")
            time.sleep(1)  # Sleep to simulate work before trying for lock1.
            with lock1:  # Lock 1 is acquired here (which task1 already holds).
                print("Task 2: Acquired lock1, completing task.")
    
    # Start the two threads that will attempt to acquire locks in conflicting orders.
    threading.Thread(target=task1).start()
    threading.Thread(target=task2).start()

@profile
def infinite_recursion():
    """Simulate infinite recursion, causing a stack overflow."""
    print("Starting infinite recursion simulation...")
    
    # This function calls itself indefinitely, consuming stack space.
    def recurse():
        print("Recursion in progress...")
        recurse()  # Call itself again, leading to an infinite recursion.
    
    recurse()  # Initiates the infinite recursion.

@profile
def resource_exhaustion():
    """Simulate resource exhaustion by creating large files repeatedly."""
    print("Starting resource exhaustion simulation...")
    
    counter = 0
    while True:
        # Create large files repeatedly, exhausting disk space.
        file_name = f'large_file_{counter}.txt'
        with open(file_name, 'w') as f:
            # Write a large amount of data to each file.
            f.write('This is a large file.' * 10**6)  # Write a very large string into the file.
            print(f"Created {file_name}. This file is consuming disk space.")
            counter += 1  # Increment the file counter for the next file.
        time.sleep(1)  # Wait 1 second before creating the next large file.

@profile
def zombie_process():
    """Simulate zombie processes by forking processes that exit without being reaped."""
    print("Starting zombie process simulation...")

    while True:
        pid = os.fork()  # Create a new child process
        if pid == 0:
            # Child process: Exit without being reaped
            print(f"Child process {os.getpid()} exiting.")
            os._exit(0)
        else:
            # Parent process: Do nothing, allowing the child process to become a zombie
            print(f"Parent process {os.getpid()} waiting for child.")
        time.sleep(1)  # Wait a second before forking another child process.

@profile
def race_condition():
    """Simulate a race condition with threads accessing shared data."""
    print("Starting race condition simulation...")

    shared_data = 0
    lock = threading.Lock()

    def thread_task():
        nonlocal shared_data
        for _ in range(100000):
            with lock:
                shared_data += 1  # Race condition: threads modifying shared data without proper synchronization
        print(f"Thread finished modifying shared data: {shared_data}")

    # Create and start multiple threads that will modify the shared data
    threads = [threading.Thread(target=thread_task) for _ in range(10)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print(f"Final value of shared data: {shared_data}")

@profile
def disk_io_saturation():
    """Simulate disk IO saturation by creating and writing to files in a loop."""
    print("Starting disk IO saturation simulation...")

    counter = 0
    while True:
        file_name = f"test_file_{counter}.txt"
        with open(file_name, "w") as f:
            # Write a large amount of data into the file
            f.write("This is some data to saturate the disk IO." * 10**6)
            print(f"Created and wrote to {file_name}.")
        counter += 1
        time.sleep(0.1)  # Slow down to avoid flooding the disk too quickly.

def exit_program():
    """Exit the program gracefully."""
    print("Exiting program gracefully...")
    sys.exit()  # Terminate the program.

def main():
    """Main menu allowing the user to choose a chaos scenario."""
    scenarios = {
        '1': memory_leak,
        '2': blocked_threads,
        '3': thread_leak,
        '4': infinite_loop,
        '5': cpu_stress,
        '6': file_descriptor_leak,
        '7': unhandled_exception,
        '8': deadlock,
        '9': infinite_recursion,
        '10': resource_exhaustion,
        '11': zombie_process,
        '12': race_condition,
        '13': disk_io_saturation,
        '14': exit_program
    }

    while True:
        print("\nChaos Scenarios Menu:")
        for key, value in scenarios.items():
            print(f"{key}. {value.__name__}")

        choice = input("Choose a scenario (1-11): ")
        if choice in scenarios:
            print(f"Starting scenario: {scenarios[choice].__name__}...\n")
            try:
                scenarios[choice]()  # Run the selected scenario.
            except Exception as e:
                print(f"An error occurred during the scenario: {e}")
        else:
            print("Invalid choice. Please select a number between 1 and 14.")

if __name__ == "__main__":
    main()

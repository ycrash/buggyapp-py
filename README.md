```markdown
# Chaos Scenario Documentation

This document provides an overview of the chaos scenarios implemented in the program. Each scenario simulates a specific type of resource exhaustion, system malfunction, or unpredictable behavior to demonstrate potential issues in a system. The scenarios are numbered 1 to 13, and each includes the expected output when the scenario is executed.

---

## How to Use the Python Script

To use the **buggypy.py** script, follow these steps:

### Prerequisites:
1. **Python**: Ensure that Python is installed on your system. You can check this by running the following command in your terminal or command prompt:
    ```
    python --version
    ```
    If Python is not installed, you can download and install it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: The script uses the `memory_profiler` library for profiling memory usage. Install it using `pip` by running:
    ```
    pip install memory_profiler
    ```

### Steps to Run the Script:

1. **Download the Script**: Save the Python script as `buggypy.py` on your local machine.

2. **Navigate to the Script Location**: Open a terminal or command prompt and navigate to the directory where the `buggypy.py` file is located. For example:
    ```
    cd /path/to/your/script/
    ```

3. **Run the Script**: Execute the script by running:
    ```
    python buggypy.py
    ```

4. **Choose a Chaos Scenario**: Once the script starts, you will be presented with a menu of chaos scenarios. Each scenario is associated with a number. For example:

    ```
    Chaos Scenarios Menu:
    1. memory_leak
    2. blocked_threads
    3. thread_leak
    4. infinite_loop
    5. cpu_stress
    6. file_descriptor_leak
    7. unhandled_exception
    8. deadlock
    9. infinite_recursion
    10. resource_exhaustion
    11. zombie_process
    12. race_condition
    13. disk_io_saturation
    14. exit_program
    ```

5. **Select a Scenario**: Type the number corresponding to the chaos scenario you wish to simulate and press Enter. For example, to simulate a memory leak, type:
    ```
    1
    ```

6. **Observe the Output**: The selected chaos scenario will run, and you will see output messages related to that scenario. Follow the expected output as described for each scenario.

7. **Exit the Program**: If you wish to exit the program, select option 14 (Exit Program) from the menu. The script will terminate gracefully.

### Example:

```
Chaos Scenarios Menu:
1. memory_leak
2. blocked_threads
3. thread_leak
...
14. exit_program

Choose a scenario (1-14): 1
Starting memory leak simulation...
Leaked 1 objects to memory.
Leaked 2 objects to memory.
...
```

---

## Chaos Scenarios

### 1. **Memory Leak**
- **Description**: This scenario simulates a memory leak by continuously allocating memory and storing large string objects in a list, causing the program's memory usage to increase over time.
- **Expected Output**:
  - Continuously prints messages about the number of leaked objects.
  - The program will eventually consume all available memory, leading to a system slowdown or crash.

    ```
    Starting memory leak simulation...
    Leaked 1 objects to memory.
    Leaked 2 objects to memory.
    ...
    ```

---

### 2. **Blocked Threads**
- **Description**: This scenario simulates multiple threads being blocked while they wait for a long task to complete.
- **Expected Output**:
  - Threads will start and simulate a long-running task (10 seconds sleep).
  - The program prints messages indicating that threads are blocked and waiting for resources.
  - After waiting, the threads will finish, and the program will print that all threads have completed.

    ```
    Starting blocked threads simulation...
    Thread started, performing a long task.
    Thread started, performing a long task.
    ...
    All threads are blocked! All threads are waiting for resources.
    All threads have finished.
    ```

---

### 3. **Thread Leak**
- **Description**: This scenario continuously creates new threads that never terminate, causing a thread leak.
- **Expected Output**:
  - New threads are started and remain active indefinitely.
  - The program continuously prints messages indicating that a new thread has been started, resulting in an ever-growing number of threads.

    ```
    Starting thread leak simulation...
    Started a new thread. Thread leak ongoing.
    Started a new thread. Thread leak ongoing.
    ...
    ```

---

### 4. **Infinite Loop**
- **Description**: This scenario runs an infinite loop that consumes CPU resources without doing any meaningful work.
- **Expected Output**:
  - The program will enter an infinite loop and consume 100% of one CPU core.
  - No further output will be generated unless the program is interrupted.

    ```
    Starting infinite loop simulation...
    ```

---

### 5. **CPU Stress**
- **Description**: This scenario simulates high CPU usage by creating multiple threads that each run an infinite loop (busy-wait).
- **Expected Output**:
  - The program will start multiple threads, each running a busy-wait loop that keeps the CPU active.
  - The CPU usage will increase significantly, potentially slowing down the system.

    ```
    Starting CPU stress simulation...
    ```

---

### 6. **File Descriptor Leak**
- **Description**: This scenario simulates a file descriptor leak by continuously opening files without closing them.
- **Expected Output**:
  - The program will repeatedly open files (e.g., `/dev/null`) without ever closing them.
  - Over time, the number of open file descriptors will increase, which can eventually exhaust the system's file descriptor limit.

    ```
    Starting file descriptor leak simulation...
    Opened a new file descriptor. File descriptor leak ongoing.
    Opened a new file descriptor. File descriptor leak ongoing.
    ...
    ```

---

### 7. **Unhandled Exception**
- **Description**: This scenario simulates a thread encountering an unhandled exception (e.g., division by zero) during execution.
- **Expected Output**:
  - A new thread starts and immediately raises a division by zero exception.
  - The exception will not be caught, causing the thread to terminate abnormally.
  - The main program will continue, but the thread will exit unexpectedly.

    ```
    Starting unhandled exception simulation...
    Thread started. Cause exception now...
    An error occurred: ZeroDivisionError: division by zero
    ```

---

### 8. **Deadlock**
- **Description**: This scenario creates a deadlock between two threads. Each thread acquires a lock and then attempts to acquire the lock held by the other thread, causing both threads to block indefinitely.
- **Expected Output**:
  - Two threads will start and attempt to acquire locks in conflicting orders.
  - The threads will become stuck, and the program will print messages indicating that each thread is waiting for the other to release the lock.

    ```
    Starting deadlock simulation...
    Task 1: Acquired lock1, now waiting for lock2.
    Task 2: Acquired lock2, now waiting for lock1.
    ```

---

### 9. **Infinite Recursion**
- **Description**: This scenario triggers infinite recursion, leading to a stack overflow.
- **Expected Output**:
  - The program will start a recursive function that calls itself indefinitely.
  - After a certain depth, a `RecursionError` will occur due to the exhaustion of the call stack.

    ```
    Starting infinite recursion simulation...
    Recursion in progress...
    Recursion in progress...
    ...
    ```

---

### 10. **Resource Exhaustion**
- **Description**: This scenario simulates disk resource exhaustion by creating large files repeatedly, consuming disk space.
- **Expected Output**:
  - The program will continuously create large files (e.g., `large_file_1.txt`, `large_file_2.txt`, etc.) and write significant amounts of data into them.
  - Over time, this will fill up the disk space, causing the system to run out of available storage.

    ```
    Starting resource exhaustion simulation...
    Created large_file_1.txt. This file is consuming disk space.
    Created large_file_2.txt. This file is consuming disk space.
    ...
    ```

---

### 11. **Zombie Process**
- **Description**: This scenario simulates zombie processes by forking new child processes that exit without being reaped by the parent process.
- **Expected Output**:
  - New child processes are created but not reaped (not waited for by the parent process), causing them to become zombie processes.
  - The parent process will continually fork new child processes.

    ```
    Starting zombie process simulation...
    Parent process 12345 waiting for child.
    Child process 67890 exiting.
    Parent process 12345 waiting for child.
    ...
    ```

---

### 12. **Race Condition**
- **Description**: This scenario simulates a race condition where multiple threads access and modify shared data without proper synchronization, potentially leading to inconsistent results.
- **Expected Output**:
  - Multiple threads will modify a shared variable (`shared_data`) without locking it.
  - The final value of the shared data may be inconsistent, depending on the thread execution order.

    ```
    Starting race condition simulation...
    Thread finished modifying shared data: 50000
    Thread finished modifying shared data: 80000


    ...
    ```

---

### 13. **Disk I/O Saturation**
- **Description**: This scenario saturates disk I/O by continuously reading and writing large files.
- **Expected Output**:
  - The program will write and read from large files repeatedly.
  - Over time, this will saturate the disk I/O, potentially slowing down the system.

    ```
    Starting disk I/O saturation simulation...
    Writing to file large_file_1.txt
    Writing to file large_file_2.txt
    ...
    ```
```

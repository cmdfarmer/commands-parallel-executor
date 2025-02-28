import multiprocessing.pool
import os
import sys
import multiprocessing
import subprocess

def apply_execute_command(command: str):
    print("Running: ", command, end='', flush=True)
    subprocess.Popen(command)


if __name__ == '__main__':
    file_name = os.path.basename(sys.argv[1])
    print(f"Executing file {file_name} in parallel")
    lines = [line for line in open(file_name)]
    pool = multiprocessing.Pool()
    for line in lines:
        pool.apply_async(apply_execute_command, (line,))
    
    pool.close()
    pool.join()

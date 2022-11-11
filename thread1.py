import threading
import time


def run_thread():
    for i in range(3):
        print(i, 'Running the thread!')
        time.sleep(1)


print('Starting the program!')
threading.Thread(target=run_thread).start()
print('Finishing the program!')

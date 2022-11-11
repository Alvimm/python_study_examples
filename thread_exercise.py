from threading import Thread
from time import sleep


def task(wait_time, message):
    print(f'\nStarting task {message}')
    sleep(wait_time)
    print(f'\nTask completion {message}')


thread = Thread(target=task, args=(2, 'Running Thread'))
thread.start()
print('\nWaiting for the Thread to run...')
thread.join()
print('\nExecution completed!!!!!!')

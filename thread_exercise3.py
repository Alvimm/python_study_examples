from threading import Thread
from time import sleep


def task1(wait_time, num, message):
    print(f'Starting task: {message}')
    sleep(wait_time)
    print(f'Result of {message}: {num ** 3}')
    print(f'Task completion: {message}')


def task2(wait_time, num, message):
    print(f'Starting task: {message}')
    sleep(wait_time)
    print(f'Result of {message}: {num ** 2}')
    print(f'Task completion: {message}')


thread1 = Thread(target=task1, args=(3, 5, 'First thread'))
thread2 = Thread(target=task2, args=(2, 5, 'Second thread'))
thread1.start()
thread2.start()
print('Waiting for the threads to run...')
thread1.join()
thread2.join()
print('Execution completed!!!!!!')

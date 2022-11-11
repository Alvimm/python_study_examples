from threading import Thread
from time import sleep


def task(wait_time, message):
    print(f'Starting task: {message}')
    sleep(wait_time)
    print(f'Task completion: {message}')


thread1 = Thread(target=task, args=(3, 'First thread'))
thread2 = Thread(target=task, args=(2, 'Second thread'))
thread1.start()
thread2.start()
print('Waiting for Threads to run..')
thread1.join()
thread2.join()
print('Execution completed!!!!!!')

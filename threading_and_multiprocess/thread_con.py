# This is I/O bound (Asynchronously)
# import threading
import concurrent.futures
import time
import subprocess

subprocess.run(['clear'])

start = time.perf_counter()

def do_something(seconds):
# def do_something():
    # print('Sleeping 1 second...')
    print('Sleeping {} second(s)...'.format(seconds))

    # time.sleep(1)
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'

    # print(f'Done sleeping...')
    # print(f'Done sleeping...{seconds}')
    
# do_something()
# do_something()
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())
    
    # secs = [5,4,3,2,1]
    # results = [executor.submit(do_something, 1) for _ in range(10)]
    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
        # print(f.result())
    
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)
    
# threads = []

# for _ in range(10):
    # t = threading.Thread(target=do_something)
    # t = threading.Thread(target=do_something, args=[1.5])
    # t.start()
    # threads.append(t)
    
# for thread in threads:
#     thread.join()

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# print(finish-start)
# print(round(finish-start, 5))

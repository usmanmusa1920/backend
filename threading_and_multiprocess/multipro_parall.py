# This is I/O bound (Asynchronously)
# import multiprocessing
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
    
# do_something(1)
# do_something(1)
    
with concurrent.futures.ProcessPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())
    
    # secs = [5,4,3,2,1]
    # results = [executor.submit(do_something, 1) for _ in range(10)]
    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)
    
    # for result in results:
    #     print(result)
    
# processes = []

# for _ in range(10):
    # p = multiprocessing.Process(target=do_something)
    # p = multiprocessing.Process(target=do_something, args=[1.5])
    # p.start()
    # processes.append(p)
    
# for process in processes:
#     process.join()
    
# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
# print(finish-start)
# print(round(finish-start, 5))

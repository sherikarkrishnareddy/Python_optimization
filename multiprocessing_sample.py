import multiprocessing
def do_task(data):
    return data*2
def start_process():
    print('Starting',multiprocessing.current_process().name)
if __name__=='__main__':
    pool_size=multiprocessing.cpu_count()*2
    pool=multiprocessing.Pool(processes=pool_size,initializer=start_process)
    inputs=list(range(10))
    outputs=map(do_task,inputs)
    print('Outputs :',outputs)
    pool.close()
    pool.join()
    

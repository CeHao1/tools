## an example

```
import torch
import torch.multiprocessing as mp
import time
import copy

def work(x):
    x1 = torch.tensor(x).to('cuda')
    x2 = x1.detach().cpu().numpy()
    # x2 = copy.deepcopy(x)
    # x2 = x
    return x2

def do_work(x, Q):
    for i in range(int(1e4)):
        work(x)
    Q.put(x)


if __name__ == "__main__":
    mp.set_start_method('spawn')

    num_processes = 10

    x = [1,2]
    Q = mp.Queue()
    
    processes = []
    for rank in range(num_processes):
        p = mp.Process(target=do_work, args=(x,Q))
        p.start()
        processes.append(p)

    t0 = time.time()
    for p in processes:
        p.join()
    
    t1 = time.time()
    print('spend time', t1-t0)
    # for i in range(num_processes):
    #     print('Q', Q.get())

```

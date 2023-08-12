from multiprocessing import Process
import multiprocessing

queue_in = multiprocessing.Queue(args.core_num) # input queue
queue_out = multiprocessing.Queue() # output queue
processes = [Process(target=function, args=(queue_in, queue_out, args,)) for _ in range(args.core_num)]


for index, file in enumerate(files):
    assert file is not None
    queue_in.put(file) # input a single file to the queue

    # block until the input queue is empty
    while not queue_in.empty():
        pass
      
# fetch cases from queue 
for i in range(len(files) * self._hp.sample_times ):
    case = queue_out.get()
    if case is not None:
        case_list.append(case)
        
# add None at the end to input queue to stop the function
for i in range(args.core_num):
    queue_in.put(None)

# join each process
for each in processes:
    each.join(1)

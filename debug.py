from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

size = comm.Get_size()
print("Hello from process", rank, "of", size)

local_data = rank * 2
local_result = local_data + 1

import time
time.sleep(local_result)

# Gather results from all processes to the root (rank 0)
all_results = comm.gather(local_result, root=0)

if rank == 0:
    print("All Results:", all_results)
    final_result = sum(all_results)
    print("Final Result:", final_result)

MPI.Finalize()


# from mpi4py import MPI

# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()

# local_value = rank + 1  # Each process has its own value (1, 2, 3, ...)
# global_sum = comm.allreduce(local_value, op=MPI.SUM)  # All processes get the sum

# print(f"Process {rank}: Local Value = {local_value}, Global Sum = {global_sum}")

# MPI.Finalize()

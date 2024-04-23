from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Use Get_rank() to get the rank
size = comm.Get_size()  # Use Get_size() to get the size

send_buf = None
recv_buf = np.empty(1, dtype=int)

# Root process
if rank == 0:
    arr = np.array([12, 21241, 5131, 1612251, 161, 6, 161, 1613, 161363, 12616, 367, 8363])
    arr.shape = (3, 4)
    send_buf = np.array_split(arr.flatten(), size)

# Scatter the send_buf among ranks
local_array = comm.scatter(send_buf, root=0)

# Calculate the local sum
local_sum = np.sum(local_array)

print(f"Local sum at rank {rank}: {local_sum}")

# Reduce local sums to the root process
global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

# Root process outputs the global sum
if rank == 0:
    print(f"Global sum: {global_sum}")from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Use Get_rank() to get the rank
size = comm.Get_size()  # Use Get_size() to get the size

send_buf = None
recv_buf = np.empty(1, dtype=int)

# Root process
if rank == 0:
    arr = np.array([12, 21241, 5131, 1612251, 161, 6, 161, 1613, 161363, 12616, 367, 8363])
    arr.shape = (3, 4)
    send_buf = np.array_split(arr.flatten(), size)

# Scatter the send_buf among ranks
local_array = comm.scatter(send_buf, root=0)

# Calculate the local sum
local_sum = np.sum(local_array)

print(f"Local sum at rank {rank}: {local_sum}")

# Reduce local sums to the root process
global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

# Root process outputs the global sum
if rank == 0:
    print(f"Global sum: {global_sum}")
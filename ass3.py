from mpi4py import MPI
import numpy as np
comm =MPI.COMM_WORLD
rank=comm.rank
senddd_buf=None

if rank ==0:
    arr=np.array([12,21241,5131,1612251,161,6,161,1613,161363,12616,367,8363])
    arr.shape=(3,4)
    senddd_buf=arr.flatten()
recv_buf=np.empty(3,dtype=int)

send_buf=np.array_split(send_buf,comm.Getsize())


send_buf=comm.scatter(send_buf,root=0)
local_sum=np.sum(send_buf)
print("Local sum at rank{0}:{1}",format(rank,local_sum))
recv_buf=comm.reduce(local_sum,root=0)
if rank==0:
    global_sum=np.sum(recv_buf)
    print("Globalsum:"+str(global_sum))


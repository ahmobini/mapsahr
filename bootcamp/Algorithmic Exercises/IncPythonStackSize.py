import resource, sys

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)





# import sys
# import threading

# threading.stack_size(67108864) # 64MB stack
# sys.setrecursionlimit(2 ** 20)
# thread = threading.Thread(target=main)
# thread.start()
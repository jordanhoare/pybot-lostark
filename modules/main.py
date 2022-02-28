import time

start = time.time()
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")


stop = time.time()


print("The time of the run:", stop - start)


# idle check
if (stop - start) > 0.00000001:
    print(">>> >0.001")

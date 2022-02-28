import time

while True:
    start_time = time.time()  # start time of the loop

    ########################
    # your fancy code here #
    ########################

    print("FPS: ", 1.0 / (time.time() - start_time))  # FPS = 1 / time to process loop

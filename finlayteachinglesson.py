import time

with open("speech.txt", "r") as fp:
    lines = [line.rstrip('\n') for line in fp.readlines()]
    for line in lines:
        time.sleep(0.001)
        print (line)
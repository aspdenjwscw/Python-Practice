import time
import threading

# Functions
def choosetypeoftimer():
    while True:
        chosentype = input("\nWhat type of timer would you like?\n1. Stopwatch\n2. Countdown\nAnswer here: ").lower()
        try:
            if chosentype == "countdown" or chosentype == "2":
                print("\nYou have chosen the countdown timer.")
                countdowntimer()
                countdowntimeplay()
                break
            elif chosentype == "stopwatch" or chosentype == "1":
                print("\nYou have chosen the stopwatch timer.")
                stopwatchtimeplay()
                break
        except:
            print("That wasn't an option.")

def countdowntimer():
    global countdowntime
    while True:
        countdowntime = input("What time would you like to countdown from? ")
        try:
            countdowntime = int(countdowntime)
            if countdowntime < 1:
                print("Please choose a number higher than {}".format(countdowntime))
            else:
                print("Alright, your countdown will now start from {}.".format(countdowntime))
                break
        except:
            print("That wasn't a number.")

def countdowntimeplay():
    global countdowntime
    print("\nStarting countdown:")
    time.sleep(1)
    while True:
        print(countdowntime)
        countdowntime -= 1
        time.sleep(1)
        if countdowntime == 0:
            print("The countdown has finished.")
            break

def stopwatchtimeplay():
    global stopwatchtime, stopwatch_running
    stopwatchtime = 0
    stopwatch_running = True
    print("\nStarting stopwatch:")
    time.sleep(1)
    
    # Start the thread to listen for stop input
    stop_thread = threading.Thread(target=stopwatch_listener)
    stop_thread.start()
    
    while stopwatch_running:
        print(stopwatchtime)
        stopwatchtime += 1
        time.sleep(1)
    
    print("The stopwatch has been stopped at {} seconds.".format(stopwatchtime))

def stopwatch_listener():
    global stopwatch_running
    input("Press Enter to stop the stopwatch.\n")
    stopwatch_running = False

# Main Code
choosetypeoftimer()

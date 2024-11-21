import time

def sleep_and_print():
    for i in range(1, 11):
        print(i)
        time.sleep(0.5)

print("Appel 1")
sleep_and_print()

print("Appel 2")
sleep_and_print()


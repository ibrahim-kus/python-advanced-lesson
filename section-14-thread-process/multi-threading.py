import time
import threading

def calculate_square(number):
    print("Executing...")

    for i in numbers:
        time.sleep(0.3)
        print("square", i * i)

def calculate_cube(number):
    for i in numbers:
        time.sleep(0.3)
        print("cube", i * i * i)

numbers = [3,7,9,27]

t = time.time()

# calculate_square(numbers)
# calculate_cube(numbers)


t1 = threading.Thread(target=calculate_square, args=(numbers,))
t2 = threading.Thread(target=calculate_cube, args=(numbers,))

t1.start()
t2.start()

t1.join() #printe geçmeden t1 in bitmesini bekle
t2.join() #printe geçmeden t2 nin bitmesini bekle
print("Executing completed:", time.time() - t)
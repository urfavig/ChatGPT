import multiprocessing as mp 
import time
import math

# Initialize empty lists to store results
results_a = []
results_b = []
results_c = []

# Function to perform calculation one on a list of numbers
def make_calculation_one(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))

#Function to perform calculation two on a list of numbers
def make_calculation_two(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number ** 4))

# Function to perform calculation three on a list of numbers
def make_calculation_three(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number ** 5))

if __name__ == '__main__':

# Generate a list of numbers
    number_list = list(range(1000000))

# Create three separate processes to perform calculations in parallel
    p1 = mp.Process(target=make_calculation_one, args=(number_list,))
    p2 = mp.Process(target=make_calculation_two, args=(number_list,))
    p3 = mp.Process(target=make_calculation_three, args=(number_list,))

    start = time.time()

# Start the processes
    p1.start()
    p2.start()
    p3.start()
    end = time.time()

# Print the time taken for parallel processing
    print(end-start)

# Store the results in temporary variables
    temp_a = results_a
    temp_b = results_b
    temp_c = results_c
    

    start = time.time()

# Perform calculations sequentially 
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)
    end = time.time()

#Print the time taken for sequential  processing
    print(end-start)

# Compare the results from parallel and sequential calculations
    print(temp_a == results_a)
    print(temp_b == results_b)
    print(temp_c == results_c)

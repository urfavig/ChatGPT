import multiprocessing as mp
import time
import math

# Define functions for performing mathematical calculations
def make_calculation_one(numbers, results):
    for number in numbers:
        results.append(math.sqrt(number ** 3))

def make_calculation_two(numbers, results):
    for number in numbers:
        results.append(math.sqrt(number ** 4))

def make_calculation_three(numbers, results):
    for number in numbers:
        results.append(math.sqrt(number ** 5))

if __name__ == '__main__':
    # Define a list of different list sizes to test
    list_sizes = [500000, 600000, 700000, 800000, 900000, 1000000, 1100000,
                  1200000, 1300000, 1400000, 1500000, 1600000, 1700000,
                  1800000, 1900000, 2000000]

    for size in list_sizes:
        number_list = list(range(size))
        
        # Create empty lists to store results from different calculations
        results_a = []
        results_b = []
        results_c = []
        
        # Create three separate processes for concurrent calculations
        p1 = mp.Process(target=make_calculation_one, args=(number_list, results_a))
        p2 = mp.Process(target=make_calculation_two, args=(number_list, results_b))
        p3 = mp.Process(target=make_calculation_three, args=(number_list, results_c))

        # Record the start time for benchmarking
        start = time.time()

        # Start the three processes concurrently
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()

        # Record the end time and calculate the execution time
        end = time.time()

        # Print the total execution time for concurrent calculations
        print(f"List size: {size}, Time of concurrent execution: {end - start:.4f} seconds")

        # Create temporary variables to store the results
        temp_a = results_a
        temp_b = results_b
        temp_c = results_c

        # Reset results lists
        results_a = []
        results_b = []
        results_c = []

        # Record the start time for non-concurrent calculations
        start = time.time()

        # Perform calculations sequentially (without multiprocessing)
        make_calculation_one(number_list, results_a)
        make_calculation_two(number_list, results_b)
        make_calculation_three(number_list, results_c)

        # Record the end time and calculate the execution time
        end = time.time()

        # Print the time taken for sequential processing
        print(f"List size: {size}, Time of sequential execution: {end - start:.4f} seconds")
        print(f"Results for list size {size} are the same: {temp_a == results_a} {temp_b == results_b} {temp_c == results_c}")
        print()

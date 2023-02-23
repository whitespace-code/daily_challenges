# Decorator to calculate the time taken by any function
# import libraries
import time
import math

# decorator to calculate duration
# taken by any function
def calculate_time_taken(func):

    # if function takes arguments,
    # they can be added,
    # like this
    def inner1(*args, **kwargs):

        # store time before function exection
        begin = time.time()

        func(*args, **kwargs)

        # store time after function execution
        end = time.time()
        print(f' -- executed \'{func.__name__}\' in {round((end - begin) * 1e6,2)} ms')

    return inner1

# Decorator to test any function against an expected result
# Test any function against an expected result
@calculate_time_taken
def test_result(func, result):
    if func == result:
        return print(f'True : [{func} = {result}]', end="")
    else:
        return print(f'False : [{func} <> {result}]', end="")

if __name__ == '__main__':
    pass

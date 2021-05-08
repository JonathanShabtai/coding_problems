from time import time

def naive_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    curr_elem = 0
    elem_0 = 0
    elem_1 = 1
    for i in range(n-1):
        curr_elem = elem_0 + elem_1
        elem_0 = elem_1
        elem_1 = curr_elem
    
    return curr_elem



def recursive_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fib(n-1) + recursive_fib(n-2)


def array_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_list = [0, 1]
    for i in range(n-1):
        fib_list.append(fib_list[-2] + fib_list[-1])

    return fib_list[-1]




def recursive_array_fib(n, recursive_list_fib = [0, 1]):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == len(recursive_list_fib) - 1:
        return recursive_list_fib[-1]
    else:
        temp = recursive_array_fib(n-2, recursive_list_fib) + recursive_array_fib(n-1, recursive_list_fib)
        recursive_list_fib.append(temp)
        return temp

def timing_functions():
    m = 32
    times_list = []

    start_time = time()
    naive_fib(m)
    end_time = time()
    times_list.append(end_time - start_time)

    start_time = time()
    recursive_fib(m)
    end_time = time()
    times_list.append(end_time - start_time)

    start_time = time()
    array_fib(m)
    end_time = time()
    times_list.append(end_time - start_time)

    start_time = time()
    recursive_array_fib(m)
    end_time = time()
    times_list.append(end_time - start_time)

    return times_list

def main():
    result = timing_functions()
    print(result)

if __name__ == '__main__':
    main()
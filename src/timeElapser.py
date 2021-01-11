import time


def print_elapsed_time(prefix=''):
    e_time = time.time()
    if not hasattr(print_elapsed_time, 's_time'):
        print_elapsed_time.s_time = e_time
    else:
        print(f'{prefix} elapsed time: {e_time - print_elapsed_time.s_time:.2f} sec')
        print_elapsed_time.s_time = e_time

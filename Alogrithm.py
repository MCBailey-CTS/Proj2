from multiprocessing import Process
from threading import Timer
from time import sleep


def search_block(proc_dict, size, memory) -> bool:
    start_index = memory.index(0, 0, MEMORY_SIZE - 1)

    current_size = 1

    for i in range(start_index + size):
        if memory[i] == 1:
            continue
        if current_size == size:
            break
        current_size += 1

    end_index = start_index + current_size

    for i in range(start_index, end_index):
        memory[i] = 1

    proc_dict[start_index] = size


def new_process(memory, size, run_time, proc_dict, start_mem):
    sleep(run_time)
    for i in range()


if __name__ == '__main__':
    timer = Timer()
    timer.start()
    MEMORY_SIZE = 10
    proc_dict = {}
    first_fit = [0] * MEMORY_SIZE
    sizes = [3, 4, 3, 1, 1, 5, 6, 7]
    times = [1, 1, 1, 1, 1, 1, 1, 1]

    processes = []

    for index in range(len(sizes)):
        process = Process(target=new_process, args=(
            first_fit, sizes[index], times[index], proc_dict, start_mem))
        processes.append(process)

    for size in sizes:
        search_block(proc_dict, size, first_fit)
        print(first_fit)

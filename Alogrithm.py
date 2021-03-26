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


if __name__ == '__main__':
    MEMORY_SIZE = 10
    proc_dict = {}
    first_fit = [0] * MEMORY_SIZE
    sizes = [3, 4, 3]

    for size in sizes:
        search_block(proc_dict, size, first_fit)
        print(first_fit)

def search_block(proc_dic, size, memory) -> bool:
    start_index = first_fit.index(0, 0, MEMORY_SIZE - 1)

    current_size = 1

    for i in range(start_index + size):
        if first_fit[i] == 1:
            continue
        if current_size == size:
            break
        current_size += 1

    end_index = start_index + current_size

    for i in range(start_index, end_index):
        first_fit[i] = 1

    proc_dict[start_index] = size


MEMORY_SIZE = 10

proc_dict = {}

first_fit = [0] * MEMORY_SIZE

print(first_fit)
#############################################
size = 3

start_index = first_fit.index(0, 0, MEMORY_SIZE - 1)

current_size = 1

for i in range(start_index + size):
    if first_fit[i] == 1:
        continue
    if current_size == size:
        break
    current_size += 1

end_index = start_index + current_size

for i in range(start_index, end_index):
    first_fit[i] = 1

proc_dict[start_index] = size
#############################################

size = 4

start_index = first_fit.index(0, 0, MEMORY_SIZE - 1)

current_size = 1

for i in range(start_index + size):
    if first_fit[i] == 1:
        continue
    if current_size == size:
        break
    current_size += 1

end_index = start_index + current_size

for i in range(start_index, end_index):
    first_fit[i] = 1

proc_dict[start_index] = size
################################################
size = 3

start_index = first_fit.index(0, 0, MEMORY_SIZE - 1)

current_size = 1

for i in range(start_index + size):
    if first_fit[i] == 1:
        continue
    if current_size == size:
        break
    current_size += 1

end_index = start_index + current_size

for i in range(start_index, end_index):
    first_fit[i] = 1

proc_dict[start_index] = size


print(first_fit)

print(proc_dict)


if __name__ == '__main__':

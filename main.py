NOT_ALLOCATED = "Not Allocated"
# Function to allocate memory to blocks as
# per worst fit algorithm


def worst_fit(block_size, m, process_size, n):

    # Stores block id of the block
    # allocated to a process

    # Initially no block is assigned
    # to any process
    allocation = [-1] * n

    # pick each process and find suitable blocks
    # according to its size ad assign to it
    for i in range(n):

        # Find the best fit block for
        # current process
        worst_index = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if worst_index == -1:
                    worst_index = j
                elif block_size[worst_index] < block_size[j]:
                    worst_index = j

        # If we could find a block for
        # current process
        if worst_index != -1:

            # allocate block j to p[i] process
            allocation[i] = worst_index

            # Reduce available memory in this block.
            block_size[worst_index] -= process_size[i]

    print("Process No. Process Size Block no.")
    for i in range(n):
        print(i + 1, "		 ",
              process_size[i], end="	 ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:

            print(NOT_ALLOCATED)

# Function to allocate memory to
# blocks as per First fit algorithm


def first_fit(block_size, m, process_size, n):

    # Stores block id of the
    # block allocated to a process
    allocation = [-1] * n

    # Initially no block is assigned to any process

    # pick each process and find suitable blocks
    # according to its size ad assign to it
    for i in range(n):
        for j in range(m):
            if block_size[j] >= process_size[i]:

                # allocate block j to p[i] process
                allocation[i] = j

                # Reduce available memory in this block.
                block_size[j] -= process_size[i]

                break

    print("Process No. Process Size	 Block no.")

    for i in range(n):
        print(" ", i + 1, "		 ", process_size[i],              "		 ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print(NOT_ALLOCATED)


# Function to allocate memory to blocks
# as per Best fit algorithm
def best_fit(block_size, m, process_size, n):

    # Stores block id of the block
    # allocated to a process
    allocation = [-1] * n

    # pick each process and find suitable
    # blocks according to its size ad
    # assign to it
    for i in range(n):

        # Find the best fit block for
        # current process
        best_index = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if best_index == -1:
                    best_index = j
                elif block_size[best_index] > block_size[j]:
                    best_index = j

        # If we could find a block for
        # current process
        if best_index != -1:

            # allocate block j to p[i] process
            allocation[i] = best_index

            # Reduce available memory in this block.
            block_size[best_index] -= processSize[i]

    print("Process No. Process Size	 Block no.")
    for i in range(n):
        print(i + 1, "		 ", processSize[i], end="		 ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print(NOT_ALLOCATED)


if __name__ == '__main__':
    ########
    print("\nworse fit")
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
    worst_fit(blockSize, m, processSize, n)

    #######
    print("\nfirst fit")
    block_size = [100, 500, 200, 300, 600]
    process_size = [212, 417, 112, 426]
    m = len(block_size)
    n = len(process_size)
    first_fit(block_size, m, process_size, n)

    #######
    print("\nbest fit")
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
    best_fit(blockSize, m, processSize, n)

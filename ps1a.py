###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    dictionary = {}
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.split(",")
            dictionary[line[0]] = int(line[1].replace("\n", ""))

    return dictionary

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    result = []
    visited = {key:1 for key in cows}
    sorted_cows = dict(sorted(cows.items(), key=lambda x: x[1], reverse=True))

    while sum(visited.values()):
        accumulated_weight = 0
        temp = []
        for cow in sorted_cows:
            if sorted_cows[cow] + accumulated_weight <= limit and visited[cow]:
                accumulated_weight += sorted_cows[cow]
                temp.append(cow)
                visited[cow] = 0
        result.append(temp)

    return result


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    Min = 999
    for partition in get_partitions(cows):
        check = 0 
        
        for subset in partition:
            acu_w = 0       
            for cow in subset:
                acu_w += cows[cow]

            if acu_w <= limit:
                check += 1


        if check == len(partition) < Min:
            res = partition
            Min = len(partition)


    return res
    
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    print("=" *50)
    cows = load_cows("ps1_cow_data.txt")
    start1 = time.time()
    print(greedy_cow_transport(cows))
    print(time.time() - start1)
    print("=" *50)
    start2 = time.time()
    print(brute_force_cow_transport(cows))
    print(time.time() - start2)
    print("=" *50)



def main():
    compare_cow_transport_algorithms()


if __name__ == "__main__":
    main()
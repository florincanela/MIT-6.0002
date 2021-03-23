
dictionary = dict()

with open("ps1_cow_data.txt", 'r') as file:
    for line in file.readlines():
        line = line.split(",")
        dictionary[line[0]] = int(line[1].replace("\n", ""))


        
        # for key, value in line.split(","):
        #     dictionary[key] = value


limit = 10
cows = dictionary


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




# from ps1_partition import get_partitions

# import time
# start = time.time()
# Min = 999
# for partition in get_partitions(cows):
#     check = 0 
    
#     for subset in partition:
#         acu_w = 0       
#         for cow in subset:
#             acu_w += cows[cow]

#         if acu_w <= limit:
#             check += 1


#     if check == len(partition) < Min:
#         res = partition
#         Min = len(partition)

# print(time.time() - start)
# print(res)

# x = res
# weight_per_subset = []
# for sub in x:
#     temp = []
#     for cow in sub:
#         temp.append(cows[cow])
#     weight_per_subset.append(sum(temp))

# print(weight_per_subset)
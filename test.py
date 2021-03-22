
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




from ps1_partition import get_partitions
MIN = 999
for partition in get_partitions(cows):
    
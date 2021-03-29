
# dictionary = dict()

# with open("ps1_cow_data.txt", 'r') as file:
#     for line in file.readlines():
#         line = line.split(",")
#         dictionary[line[0]] = int(line[1].replace("\n", ""))


        
#         # for key, value in line.split(","):
#         #     dictionary[key] = value


# limit = 10
# cows = dictionary


# result = []
# visited = {key:1 for key in cows}


# sorted_cows = dict(sorted(cows.items(), key=lambda x: x[1], reverse=True))
# while sum(visited.values()):
#     accumulated_weight = 0
#     temp = []
#     for cow in sorted_cows:
#         if sorted_cows[cow] + accumulated_weight <= limit and visited[cow]:
#             accumulated_weight += sorted_cows[cow]
#             temp.append(cow)
#             visited[cow] = 0
#     result.append(temp)




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



    




# import random

# egg_weights = (1, 5, 10, 25)
# n = 99
# print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
# print("Actual output:", dp_make_weight_recursion_v1(egg_weights, n))




# from time import time
# def fastfib(n, memo = {}):
#     if n == 1 or n == 0:
#         return 1
#     try:
#         return memo[n]
#     except KeyError:
#         result =  fastfib(n-1, memo) + fastfib(n-2, memo)
#         memo[n]  = result
#         return result


# def fib(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)



# x = time()
# for n in range(20000):
#     print(fastfib(n))
# print("="*50)
# print(time() - x)
# print("="*50,end="\n\n\n\n")
# x2 = time()
# for n in range(35):
#     print(fib(n))
# print("="*50)
# print(time() - x2)

# def fizbuzz(n):
    
#     output = ""
#     if n % 3 == 0:
#         output += "Fizz"

#     if n % 5 == 0:
#         output += "Buzz"

#     if not output:
#         output = n

#     return output


# for n in range(1, 100):
#     print(fizbuzz(n))


#can't figure out how to implement dynamic programming
def dp_make_weight_recursion_v1(egg_weights, target_weight):
    if target_weight < 1:
        return target_weight 

    elif target_weight >= egg_weights[-1]:
        target_weight -= egg_weights[-1]
        return 1 + dp_make_weight_recursion_v1(egg_weights, target_weight)

    elif target_weight < egg_weights[-1]:
        return dp_make_weight_recursion_v1(egg_weights[:-1], target_weight)

#alot better but still no dynamic programming
def dp_make_weight_recursion_v2(egg_weights, target_weight, memo = {}):
    if target_weight < 1:
        return target_weight

    return (target_weight // egg_weights[-1]) + dp_make_weight_recursion_v2(egg_weights[:-1], 
                                                            (target_weight % egg_weights[-1]))
    

print(10 % 25)
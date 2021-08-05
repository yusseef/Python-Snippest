#Itertools: product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator
List = [1, 2, 3]
List_2 = [4, 5]
Prod = product(a, b) #Combine all posible combination RESULT5 [(1, 2), (1, 4), (2, 3), (2, 4)]
Prod = product(a, b, repeat=2) #Combine all posible combination with repeated values

Perm = permutations(List) #Return all possible permutations of the list
Perm = permutations(List, 2) #Return all possible permutations of the list with two values

List_2 = [1, 2, 3 , 4]
comb = combinations(List_2, 2) #Return all possible combinations
Comb = combinations_with_replacement(List_2, 2) #return all possible values even if repeated
#Diffrence between permutaions and combination is that permutation order matters

Acc = accumulate(List_2)#Return the accumulate sum of the list
Acc = accumulate(List_2, func=operator.mul)#Return the accumulate multiple of the list
Acc = accumulate(List_2, func=max)#Return the accumulate max item of the list

def smaller_than_3(x):
    return x < 3

Group = groupby(List_2, key=smaller_than_2) #Return a key of True to elements smaller than 3 and False for elements bigger than 3
Group = groupby(List_2, key=lambda x : x < 3) #Return a key of True to elements smaller than 3 and False for elements bigger than 3


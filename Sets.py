# Sets: unorderd, mutable, no duplicates

Set = {1, 2, 3} #Declare a set by {}
Set = set("Hello") #Declare a set by a function set
Set.add(4) #To add an item
Set.remove(4) #To remove an item
Set.discard(4) #Another way to remove an elemnt
Set.clear() #Clear all set
#Set.pop() #Remove the first item 

'''Union, intersection and diffrence'''
primes = {2, 3, 5, 7, 11}
evens = {2, 4, 6, 8, 10}
Union = primes.union(evens) #Return a set of the Union
Intesection = primes.intersection(evens) #Return a set of the intesection
Diffrence = primes.difference(evens) #Return the elements in first set that not in second set
Symentic = primes.symmetric_difference(evens) #Return elements from two sets but not the elemnts in both sets


primes.update(evens) #Update primes to add even elements to it
primes.intersection_update(evens) #Update primes to keep all the elements results from intersection
primes.difference_update(evens) #Update primes to keep elements from diffrence result
primes.symmetric_difference_update(evens) #Update primes to keep the elements from two sets execluding elemnts in both sets

Set_1 = {1, 2, 3, 4, 5, 6}
Set_2 = {1, 2, 3}

Set_1.issubset(Set_2) #Return True if all elemnts in Set_1 in Set_2
Set_1.issuperset(Set_2) #Opposite of subset
Set_1.isdisjoint(Set_2) #Return true if there is no intersection

Set_copy = Set_1.copy() #Copy the set into another set

Frozen = frozenset([1, 2, 3]) #cant be change after creation
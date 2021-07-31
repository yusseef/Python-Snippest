                                            #LISTS

#Lists: ordered, mutable, allows duplicate items

List_1 = ["banana", "strawberry", "apply"] #Ordered
List_2 = [5, "apple", True] 
List_3 = ["apple", "apple"] #Allows duplicate elements

item = List_1[0] #To print specific item, HINT: indexing starts with zero.

item = List_1[-1] #Get last item in the list

[print(x) for x in List_1] #You can use list comprehinsion to print list elements

if "banana" in List_1:
    print('yes')  #Determine which the item in the list or not

len(List_1) #Return number of items in the list

List_1.append("Lemon") #Insert new item in the end of the list HINT: MUTABLE

List_1.insert(0, "Peach") #insert item at specific index

List_1.pop() #Delete last item 

List_1.remove("banana") #Delete specific item

List_1.clear() #Remove all items

List_1.reverse() #REVERSE

List_1.sort() #SORT HINT:Change elements in place

List_4 = [0] * 5 #Lists can be multiple, RESULT: [0, 0, 0, 0, 0]

List_5 = [1, 2, 3, 4, 5]

Result_list = List_4 + List_5 #Lists can be added to each other

'''SLICING'''
Slicing_list = Result_list[1:5] #Print a numbers from index 1 to index 5 execluding the last index
Slicing_list = Result_list[:5] #Print a numbers from the beginning to index 5 execluding the last index
Slicing_list = Result_list[1:] #Print a numbers from index 1  to the end 
Slicing_list = Result_list[::2] #Print a numbers from begining with two steps at each
Slicing_list = Result_list[::-1] #REVERSE

'''COPYING'''

Copy = Result_list.copy()










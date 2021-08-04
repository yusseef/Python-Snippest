#Collections: Counter, namedtuple, OrderedDict, defaultDict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
a = "aaaaaaabbbbbcccccc"
Counter = Counter(a) #Return count of each elemnt in the str
Counter.items() #Return the result in a list
Counter.keys()#Return list of the keys ex: a, b, c
Counter.values() #return list of the values ex: 4, 4, 4
Counter.most_common(1)[0][0] #return first most repeated item


Point = namedtuple('Point', 'x, y') #Create a class called point with element x, y
pt = Point(1, -4) #To assign the values


ordered_dict = OrderedDict() #Regular dict but remember the order inserted
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

#Note: Python 3.7 and above allows regular dictionaries to be ordered

default = defaultdict(int) #Allows to give a default value to item not in the dictionary
default['a'] = 1
default['b'] = 2
default['c'] = 3
default['d'] = 4


deque = deque() #Append items either in the beginning or the last 
deque.append(1)
deque.append(2) #Add to the last
deque.appendleft(3) #Add to the beginning
deque.pop() #remove from the last
deque.popleft() #Remove from the beginning
deque.clear() #remove all elements
deque.extend([6, 7]) #Add more than an elements to the end
deque.extendleft([6, 7]) #Add more than items to the first of the list
deque.rotate(1) #Rotate all elemnts one place to the right
deque.rotete(-1) #Rotate all elements one place to the left


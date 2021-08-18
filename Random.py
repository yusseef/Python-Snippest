import random
Random = random.random() #Print a random float from 0 to 1 EX: 0.504015320
Random = random.uniform(1, 10) #Print a random float value from 1 to 10 EX: 5.6842986054521
Random = random.randint(1, 10) #Print int value from 1 to 10 EX: 7
Random = random.randrange(1, 10) #Orint int value from 1 to 9 execlude 10
Random = random.normalvariate(0, 1)#For statistics return normal distribution value

List = list("ABCDEFGH")
Random = random.choice(List) #Return random value from the list
Random = random.choice(List, k= 3) #Return three random value from the list repeat not allowed
Random = random.choices(List, k= 3) #Return three random value from the list repeat allowed
Random = random.shuffle(List) #Shuffle a list

'''Random seed'''
random.seed(1) #Seed allows yu to get a random value but not changeable each time you run the code
random.random()
random.randint(1, 10)

'''Secrets'''
import secrets #Use for passwords and authentications

Secret = secrets.randbelow(10)#Random number from 1 to 9 execlude 10

'''numpy'''
import numby as np
Num = np.random.rand(3) #Return an array with random floats
Num = np.random.rand(3, 3) #Return an array with random floats 3, 3 dimensionall array
Num = np.random.randint(1, 10, 3)#Return integer array from 1 to 10 with size of three
Num = np.random.randint(1, 10, (3, 4))#Return integer array from 1 to 10 with size of 3, 4


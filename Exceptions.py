#Errors and exceeptions
a = 5 print(5) #Syntax error
a = 5 + '10' #Type error
import somemoduel #ModeleNotFoundError
b = c #NameError
f = open('file.txt') #FileNotFoundError
a = [1, 2, 3]
remove(4)#ValueError
a[4] #IndexError

'''Exceptions'''
x = -5
if x < 0:
    raise Exception('Negative value')

assert(x <= 0) , 'Negative value' #AssertionError

try:
    a = 5 / 0
except :
    print('error')

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
    a = 5 / 0 #No divide by zero allowed
except :
    print('error')


try:
    a = 6 / 0
    b = a + '10'
except Exception as e:
    print(e) #Will print the error as a string

except TypeError:
    print('error') #You can determine the error type

else: #Runs when there is no errors
    print('no error')

finally:#Runs always
    print('always run')


'''define ur own exceptions'''

class TooHighValueError(Exception):
    pass

def test(x):
    if x > 500:
        raise TooHighValueError('VAlue is too high')

test(700) #Return VAlue is too high


try:
    test(700)
except TooHighValueError:
    print('Value is too high') #Return Value is too high
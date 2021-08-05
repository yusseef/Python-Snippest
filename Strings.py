#Strings: ordered, immutable, text representation
String = "Hello world"
String = 'I\'m developer' #To put ' 
Multiline_String = """Hello
World
Yussef
"""
Char = String[0] # To access the first charachter
String[-1] #To access last charachter

'''Slicing'''

String[1:5] #Acces the charachters from index 1 to 5 execluding 5
String[:5] #Acces the charachters from index 0 to 5 execluding 5
String[:] #Acces all string
String[::1] #Acces all string
String[::2] #Acces String by 2 steps
String[::-1] #Reverse


String_1 = "Hello"
String_2 = "Yussef"
Sentence = String_1 + String_2 #RESULT = Hello Yussef

for Char in String_1: #Iterate
    print(Char)

String_Whitespace = '    yussef   '
String_Whitespace.strip() #Remove the white space

String.upper() #Convert to uppercase
String.lower() #Convert to lowercase
String.startswith('H') #To check if string starts with specific character or sentence
String.endswith('H') #To check if string endss with specific character or sentence
String.find('H') #Return the first index of the character or subcharacter
String.count('H')#Count how many strings or substrings
String.replace('Hello', 'Hi') #Replace hello with hi HINT:REturns a new string and not change the original one
String.split() #Split each word HINT: you can change the delimeter DEFAULT is space
Fromlist_Tostring = ''.join(String)

'''%, format(), f-string'''
var = 3.12456
String = "the number is %d" %var #Result will be 3 DECIAML
String = "the number is %f" %var #Result will be 3.123457 Float
String = "the number is .%2f" %var #Result will be 3.12 Float

String = "the number is {}".format(var) #Result will be 3.123457 Float
String = "the number is {:.2f}".format(var) #Result will be 3.12 Float

String = f"the number is {var}"#REsult will be 3.1234567










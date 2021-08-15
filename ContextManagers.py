#Example 1 
with open('note.txt', 'w') as file: #This will make sure that the file closed after the editing
    file.write('Hello')    

#Example 2 
from threading import Lock
lock = Lock()
with lock: #Dont need to do lock.release()
    #.....
    pass

#Example 3 in classes

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            file.close()
        print('exit')

with ManagedFile('notes.txt') as file:
    file.write('some names')
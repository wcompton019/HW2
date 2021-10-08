# HW2: Stack

# Budget 10+ hours by Oct. 8 to complete this assignment if you received an autograder score of less than 50 on HW1.

# You may use code from class or prior assignments, but may not use internal Python data structures such as lists or arrays.
# You are strongly encouraged to use a Linked List. You can include a Linked List (sub)class inside this class, or use "import".

# Stacks implement a first-in-last-out storage. Only the most recently added (pushed) element may be seen (using peek) or removed (pop)
# This behavior is tested by the autograder.
# Do not submit an assignment that does not complete the autograder without triggering an error message.
# The provided code, as is, meets this requirement.

# This assignment's solutions will not be covered in class, but the assignment will be eligible for resubmission.
# Instead this assignment is MANDATORY:
# I will require submission of a version of HW2 (or HW1) that receives a 100 from the autograder to submit your final grade.
# You may collaborate with classmates or use online resources, but please cite all sources of help after this comment:

class Stack:
    def __repr__(self):
        # Provided
        if self.__next != None:
            return "(" + str(self.__data) + ")->" + self.__next.__repr__()
        else:
            return str(self.__data)
    def __str__(self):
        # Provided
        return self.__repr__()
    # an initializer to create a new stack object
    def __init__(self, initarg = None, initnext = None):
        self.__data = initarg
        self.__next = initnext
        self.__Size = 0
        
    # given some data, update the stack to include that data
    # input: data
    # output: nothing
    # side effect: data is now the first piece of data in the stack
    def push(self,data):
        if self.__data == None:
            self.__data = data
            self.__Size += 1
            return self
            
        elif self.__next != None:
            self.__next == self.__next.push(self.__data)
            self.__data = data
            self.__Size += 1
            return self
        
        elif self.__data != None:
            self.__next = Stack().push(self.__data)
            self.__data = data
            self.__Size += 1
            return self  #not needed forautograder, but helped visualise what was happening and could not get to work without return statement
        
    # return the first piece of data without altering the stack
    # input: nothing
    # output: data
    # side effect: none
    def peek(self):
        return self.__data
        
    def next(self):
        return self.__next.__data
    # remove and return the first piece of data in the stack
    # input: nothing
    # output: data
    # side effect: data is no longer in stack
    def pop(self):
        if self.__data == None:
            return None
            
        if self.__next != None:
            da = self.__data
            self.__data = self.__next.pop()
            self.__Size -= 1
            return da
            
        else:
            last = self.__data
            #print(self.__data)
            self.__data = None
            self.__Size -= 1
            return last
    
    # return True if there is no data in the stack
    def empty(self):
        return self.__Size == 0
        
    # return the number of data objects currently in the stack
    def size(self):
        return self.__Size
        
#I got some help from Will Reeves with the last section of pop
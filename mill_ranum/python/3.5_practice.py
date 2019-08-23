# practice manually implementing a Stack in python
# differentiate a ADT from its implementation, i.e. data structures
# four ADTs: stacks, queues, deques, lists
# a stack ADT can be implemented thru python list[]
# a stack is LIFO


class Stack:
    def __init__(self):
        self.items = []  # initiat state as an empty list
   
   #check if stack is empty
    def isEmpty(self):
        return self.items == [] # return a bool

    # add an item to a stack
    def push(self, item):
        self.items.append(item)
    
    # remove an item from top
    def pop(self,item):
        return self.items.pop()  # return the modified stack
    #*** cannot pop from an empty list
    
    # get last item from stack
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack() # create a stack object
for i in range(len('I am a stack')):
    s.push(i)

print(s.size())

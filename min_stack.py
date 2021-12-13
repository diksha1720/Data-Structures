# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
 


class MinStack:

    def __init__(self):
        self.t=-1
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.t+=1
        

    def pop(self) -> None:
        self.stack.pop()
        self.t-=1
        

    def top(self) -> int:
        return self.stack[self.t]
        

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
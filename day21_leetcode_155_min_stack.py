class MinStack(object):
    # REVISION NOTES:
    # Goal: Design a stack that retrieves the minimum element in O(1) time.
    # Approach: 
    # - Use an auxiliary stack (`min_stack`) to keep track of the minimum element at each level of the main stack.
    # - Both stacks must be modified in sync during push and pop operations so that the top of 
    #   `min_stack` always represents the minimum element for the current state of `stack`.
    # Complexity:
    # - Time Complexity: O(1) for push, pop, top, and getMin.
    # - Space Complexity: O(N) to store values in stacks.

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, value):
        # Always push the value to the main stack
        self.stack.append(value)
    
        # Push to min_stack:
        # If min_stack is empty or the new value is less than the current minimum, 
        # push the new value. Otherwise, duplicate the current minimum value.
        if not self.min_stack or value < self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        # Pop from both stacks to maintain synchronization
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        # Return the top element of the main stack in O(1)
        return self.stack[-1]

    def getMin(self):
        # Return the current minimum element in O(1)
        return self.min_stack[-1]
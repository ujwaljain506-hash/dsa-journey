class Solution(object):
    # REVISION NOTES:
    # Goal: Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).
    # Approach:
    # - Use a stack to store operands (numbers).
    # - Iterate through the tokens:
    #   - If token is an operator (+, -, *, /), pop the top two numbers from the stack.
    #     Note: The second popped number is the left operand (a), and the first is the right operand (b).
    #   - Perform the operation and push the result back. Division should truncate toward zero.
    #   - If token is a number, convert it to an integer and push it onto the stack.
    # - The final remaining element in the stack is the result.
    # Complexity:
    # - Time Complexity: O(N) where N is the number of tokens.
    # - Space Complexity: O(N) to store operands in the stack.

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in "+-*/":
                # Pop operands (note the order: second popped is left operand, first popped is right operand)
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    # Division must truncate toward zero (e.g., 6 / -132 should be 0)
                    result = int(float(a) / float(b))
                stack.append(result)
            else:
                # Token is a number, push it onto the stack
                stack.append(int(token))

        return stack[0]
"""
File: arithExp.py
A program for evaluating arithmetic expressions.
"""

from liststack import ListStack


def infix_to_postfix(infix_exp):
    """ Converts infix expression to postfix expression.
    Return postfix expression. Operands/operators
    are separated by spaces in expressions."""
    empty_stack = ListStack()
    postfix_expression = list()

    supported_operators = ["+", "-", "*", "/", "("]
    high_operators = ["*", "/"]

    infix_exp = infix_exp.split()
    for ch in range(len(infix_exp)):
        # Created a conditional for helping identify high operators
        if len(empty_stack) > 0:
            peek = empty_stack.peek()
        else:
            peek = ""

        # Pushing all operators after encountering a high operator
        if (peek in high_operators) and (infix_exp[ch] not in ["(", ")"]):
            postfix_expression.append(infix_exp[ch])
            for op in range(len(empty_stack), 0, -1):
                item = empty_stack.pop()
                postfix_expression.append(item)

        elif infix_exp[ch] in supported_operators:
            empty_stack.push(infix_exp[ch])

        # When encountering a right parenthesis ...
        elif infix_exp[ch] == ")":
            counter = len(empty_stack) - 1
            # ... push operators until meet a left parenthesis
            while counter > 0 and empty_stack.peek() != "(":
                item = empty_stack.pop()
                postfix_expression.append(item)
                counter -= 1
            if empty_stack.peek() == "(":
                empty_stack.pop()
        else:
            postfix_expression.append(infix_exp[ch])

    # Check if the stack is empty before finishing the expression
    if len(empty_stack) > 0:
        for item in empty_stack:
            postfix_expression.append(item)

    # Created a variable for storing the required string
    expression = ""
    for ch in postfix_expression:
        expression += ch
        expression += " "

    return expression


def main():
    infix = "4 + 5 * 6 - 3"
    postfix = infix_to_postfix(infix)
    print("Infix expression:", infix)
    print("postfix expression:", postfix)
    print()

    infix = "( 4 + 5 ) * ( 6 - 3 )"
    postfix = infix_to_postfix(infix)
    print("Infix expression:", infix)
    print("postfix expression:", postfix)
    print()


if __name__ == "__main__":
    main()

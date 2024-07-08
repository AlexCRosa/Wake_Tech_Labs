"""
File: arithExp.py
A program for evaluating arithmetic expressions.
"""

from liststack import ListStack

def infix_to_postfix(infix_exp):
    """ Converts infix expression to postfix expression.
    Return postfix expression. Operands/operators
    are separated by spaces in expressions."""
    pass

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


if __name__ == "__main__":
    main()

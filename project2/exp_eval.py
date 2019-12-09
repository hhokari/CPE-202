#
#Emily Gavrilenko
#015218875
#4/23/2019
#
#Project2
#Section 12

from stack_array import Stack

class PostfixFormatException(Exception):
    pass

# evaluates an input postfix expression
def postfix_eval(input_str):
    # create a stack for storing operands
    stack = Stack(30)
    # change the input string to a list of input operands and operators
    list = input_str.split()

    # steps through every operator and operand in the input string
    for i in list:
        # adds operands to the stack
        try:
            float(i)
            stack.push(i)
            if len(list) == 1:
                stack.push(float(stack.pop()))
        except ValueError:
            # checks to see if the object is an operator
            if i in ["+", "-", "*", "/", "**", "("]:
                # checks to see if there are enough operands in the stack to perform the operation
                try:
                    val1 = float(stack.pop())
                    val2 = float(stack.pop())
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")

                # adds the top two items in the stack
                if i == "+":
                    stack.push(val2 + val1)

                # subtracts the top two items in the stack
                if i == "-":
                    stack.push(val2 - val1)

                # divides the top two items in the stack
                if i == "/":
                    # raises ValueError if there is division by zero
                    if val1 == 0:
                        raise ValueError
                    stack.push(val2 / val1)

                # multiplies the top two items in the stack
                if i == "*":
                    stack.push(val2 * val1)

                # exponentiates the top two items in the stack
                if i == "**":
                    stack.push(val2**val1)

            if i in ["<<", ">>"]:
                # checks to see if there are enough operands in the stack to perform the operation
                # if the value is a float, raises "Illegal bit shift operand" error
                try:
                    val1 = float(stack.pop())
                    val2 = float(stack.pop())
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
                if val1%1 !=0 or val2%1 !=0:
                    raise PostfixFormatException("Illegal bit shift operand")

                # shifts the second value in the stack by val1 places
                elif i == "<<":
                    stack.push(int(val2)<<int(val1))

                # shifts the second value in the stack by val1 places
                elif i == ">>":
                    stack.push(int(val2)>>int(val1))

            else:
                # check to see if i isn't an operator
                if i not in ["+", "-", "*", "/", "**", "(", "<<", ">>"]:
                    # checks to see if i isn't an integer operator
                    try:
                        int(i)
                    # if i isn't an integer or an operator, it is an invalid token
                    except ValueError:
                        raise PostfixFormatException("Invalid token")

    # if there are still operands in the stack when there are no more operators, raises exception "Too many operands"
    if stack.size() != 1:
            raise PostfixFormatException("Too many operands")

    # returns the evaluated postfix expression
    return stack.pop()

# converts an infix expression to a postfix expression
def infix_to_postfix(input_str):
    # create a stack for storing operands and operators
    stack = Stack(30)
    # change the input string to a list of input operands and operators
    input_list = input_str.split()
    # creates a list to store the output postfix expression
    output_list = []

    # steps through every operator and operand in the input string
    for i in input_list:
        # adds i to the output postfix list if it is an operand
        try:
            float(i)
            output_list.append(i)
        except ValueError:
            # checks to see if i is an operator
            if i in ["+", "-", "*", "/", "**", "(", "<<", ">>"]:
                # adds i to the stack if the stack size is zero
                if stack.size() == 0:
                    stack.push(i)

                # adds i to the stack if an opening parenthesis is on the stack
                elif stack.peek() == "(":
                    stack.push(i)

                # checks for priority for + and - operators
                elif i in ["+", "-"]:
                    # pops all operators with similar or higher priority and adds them to the output postfix expression
                    while (stack.size() > 0) and (stack.peek() in ["+", "-", "*", "/", "**", ">>", "<<"]):
                        output_list.append(stack.pop())
                    # adds the operator i to the stack
                    stack.push(i)

                # checks for priority for * and / operators
                elif i in ["*", "/"]:
                    # pops all operators with similar or higher priority and adds them to the output postfix expression
                    while (stack.size() > 0) and (stack.peek() in ["*", "/", "**", ">>", "<<"]):
                        output_list.append(stack.pop())
                    # adds the operator i to the stack
                    stack.push(i)

                # checks for priority for the ** operator
                elif i == "**":
                    # pops all operators with similar or higher priority and adds them to the output postfix expression
                    while (stack.size() > 0) and (stack.peek() in [">>", "<<"]):
                        output_list.append(stack.pop())
                    # adds the operator i to the stack
                    stack.push(i)

                # checks for priority for shift operators
                elif i in ["<<", ">>"]:
                    # pops all operators with similar or higher priority and adds them to the output postfix expression
                    while (stack.size() > 0) and (stack.peek() in [">>", "<<"]):
                        output_list.append(stack.pop())
                    # adds the operator i to the stack
                    stack.push(i)

                # adds i to the stack if it's an opening parenthesis
                elif i == "(":
                    stack.push(i)

            # checks if i is a closing parenthesis
            if i == ")":
                # pop all operators until an opening parenthesis is reached
                while stack.peek() != "(":
                    operator = stack.pop()
                    output_list.append(operator)
                # pops the opening parenthesis
                if stack.peek() == "(":
                    stack.pop()

    # after the loop goes through the entire input string,
    # all remaining items in the stack are popped and added to the output postfix expression
    while stack.size() != 0:
        output_list.append(stack.pop())
    # joins the list of output characters into a string
    output = ' '.join(output_list)
    # returns the postfix expression
    return output

# converts from prefix expressions to postfix expressions
def prefix_to_postfix(input_str):
    # creates a stack to store operators, operands, and joined expressions
    stack = Stack(30)
    # change the input string to a list of input operands and operators
    input_list = input_str.split()
    # creates a list to store the postfix expression
    output_list = []

    # steps through the input list in reverse
    for i in input_list[::-1]:
        # adds operands to the stack
        try:
            float(i)
            stack.push(i)
        except ValueError:
            # checks if i is an operator
            if i in ["+", "-", "*", "/", "**", "(", "<<", ">>"]:
                # removes the top two values of the stack and adds the operator i to the end
                val1 = stack.pop()
                val2 = stack.pop()
                add = val1 + " " + val2 + " " + i
                # adds the new expression to the stack
                stack.push(add)

    # after the loop goes through the entire input string,
    # all items in the stack are popped and added to the output postfix expression
    while stack.size() != 0:
        output_list.append(stack.pop())
    # joins the list of output characters into a string
    output = ' '.join(output_list)
    # returns the postfix expression
    return output

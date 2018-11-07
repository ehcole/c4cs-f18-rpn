#!/usr/bin/env python3

import operator
import readline
import colorama

operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        'q': "quit"
    }
def calculate(myarg):
    stack = list()
    userinput = str()
    for token in myarg.split():
        try:
            num = int(token)
        except:
            userinput += colorama.Back.GREEN + token + colorama.Style.RESET_ALL + " "
        else:
            if num < 0:
                userinput += colorama.Style.BRIGHT + colorama.Fore.RED + token + colorama.Style.RESET_ALL + " "
            else:
                userinput += token + " "
    print("user input:", userinput)
    print("Stack:")
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            #if token == "q":
            #    exit(0)
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
#            stack.append('^')c
        for item in stack:
            try:
                num = int(item)
            except:
                print(colorama.Back.GREEN + item)
            else:
                if num < 0:
                    print(colorama.Style.BRIGHT + colorama.Fore.RED + str(num))
                else:
                    print(str(num))
            print(colorama.Style.RESET_ALL)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()
    
def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
            print("Result: ", colorama.Style.BRIGHT + colorama.Fore.RED + str(result))
            print(colorama.Style.RESET_ALL)
        else:
            print("Result: ", result)
        
if __name__ == '__main__':
    main()
                                                                                                                                                

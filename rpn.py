#!/usr/bin/env python3

def calculate(arg):
    stack = []
    tokens = arg.split(" ")
    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            stack.append(result)
    return stack[0]
    
            
    
def main():
    while True:
        print(calculate(input("rpn calc> ")))
        

if __name__ == '__main__':
    main()


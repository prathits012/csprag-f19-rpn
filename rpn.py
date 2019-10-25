#!/usr/bin/env python 3

def calculate(arg):
    stack=list()
    for token in arg.split():
        if token =='+':
            arg2=stack.pop()
            arg1=stack.pop()
            result = arg1+arg2
            stack.append(result)
        if token =='-':
            arg2=stack.pop()
            arg1=stack.pop()
            result = arg1-arg2
            stack.append(result)
        else:
            stack.append(int(token))
        print(stack)
    return stack.pop()
def main():
    while True:
        calculate(input("rpn calc> "))
    if __name__ == '__main__':
        main()

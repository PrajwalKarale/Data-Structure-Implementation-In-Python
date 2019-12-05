def parenthesis_checker(eq):
    open_brackets = ['(','{','[']
    close_brackets = [')','}',']']
    stack = []
    exp = eq
    for i in exp:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if len(stack) > 0 and open_brackets[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return 'UNBALANCED'
    if len(stack) == 0:
        return 'BALANCED'
def main():
    #taking input of the expression'
    eq = input('Enter the expression: ')
    print(f'The expression is {eq}')
    message = parenthesis_checker(eq)
    print(f'The given expression {eq} is {message}')
main()

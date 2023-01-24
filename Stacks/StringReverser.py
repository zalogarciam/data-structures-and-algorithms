def reverse_string( string):
    stack = []
    result = ""
    for i in range(len(string)):
        stack.append(string[i])
    for i in range(len(stack)):
        result += stack.pop()
    print(result)

reverse_string("abcd")
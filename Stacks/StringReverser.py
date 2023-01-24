def reverse_string(string):
    if string is None:
        raise Exception("String is none")
    stack = []
    result = ""
    for i in range(len(string)):
        stack.append(string[i])
    for i in range(len(stack)):
        result += stack.pop()
    print(result)

reverse_string("abcd")
reverse_string(None)
reverse_string("")
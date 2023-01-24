def balanced_expression(string):
    open_list = "([<"
    close_list = ")]>"
    stack = []
    for character in string:
        if character in open_list:
            stack.append(character)
        if character in close_list:
            if len(stack) == 0: return False
            open_character = stack.pop()
            if open_list.index(open_character) != close_list.index(character):
                return False
    if len(stack) > 0: return False
    return True

print(balanced_expression("1 + 2"))
print(balanced_expression(""))
print(balanced_expression("("))
print(balanced_expression("1 + 2)))"))
print(balanced_expression("(1 + 2)))"))
print(balanced_expression("(1 + 2)"))
print(balanced_expression("(1 + 2"))
print(balanced_expression("(([1] + <2>))[a]"))
print(balanced_expression("((<1] + <2>))[a]"))
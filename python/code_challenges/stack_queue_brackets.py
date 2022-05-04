from data_structures.stack import Stack
import re

def multi_bracket_validation(string):
    pairs = {']':'[', '}':'{', ')':'('}
    regex_string = re.findall('[{}\[\]()]', string)
    joined_string = "".join(regex_string)
    new_stack = Stack()
    for char in joined_string:
        if char not in pairs:
            new_stack.push(char)
        else:
            if new_stack.top == None:
                return False
            if new_stack.top.value == pairs[char]:
                new_stack.pop()
            else:
                return False
    if new_stack.is_empty:
        return True
    else:
        return False

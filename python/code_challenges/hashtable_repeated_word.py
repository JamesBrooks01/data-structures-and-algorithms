from collections import Counter
import re

def first_repeated_words(str):
    if str == '':
        return None
    lowercase_input = str.lower()
    punct_removed = re.sub('[^\w\s\’]','',lowercase_input)
    split = punct_removed.split(' ')
    counted = Counter(split)
    first_repeat = None
    num_to_zero_two = 100
    for x in counted:
        if counted[x] > 1:
            first_index = split.index(x)
            split.pop(first_index)
            second_index = split.index(x)
            split.insert(first_index, x)
            if second_index < num_to_zero_two:
                first_repeat = x
                num_to_zero_two = second_index

    return first_repeat

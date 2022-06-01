from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    values = tree1.in_order()
    values2 = tree2.in_order()
    hash1 = Hashtable()
    hash2 = Hashtable()
    same_values = set()
    for num in values:
        hash1.set(f"{num}",num)
    for num in values2:
        hash2.set(f'{num}', num)
    hash1_keys = hash1.keys()
    for key in hash1_keys:
        if hash2.contains(key):
            value = hash1.get(key)
            same_values.add(value)
    return same_values

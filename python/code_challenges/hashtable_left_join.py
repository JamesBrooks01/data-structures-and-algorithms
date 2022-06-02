def left_join(left, right):
    return_list = []
    for item in left:
        item_list = []
        item_list.append(item)
        value = left[item]
        item_list.append(value)
        if item in right:
            value2 = right[item]
            item_list.append(value2)
        else:
            item_list.append("NONE")
        return_list.append(item_list)
    return return_list

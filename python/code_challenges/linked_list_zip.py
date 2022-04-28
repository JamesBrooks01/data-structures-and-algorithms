from data_structures.linked_list import LinkedList

def zip_lists(a, b):
    new_list = LinkedList()
    current_1 = a.head
    current_2 = b.head
    if a.head == None:
        return b
    if b.head == None:
        return a
    new_list.insert(current_1.value)

    while new_list:
        if current_1.next == None and current_2.next == None:
            new_list.append(current_2.value)
            break
        if current_1.next == None and current_2.next != None:
            new_list.append(current_2.value)
            next_value = current_2.next
            new_list.append(next_value.value)
            break
        if current_1.next != None and current_2.next == None:
            new_list.append(current_2.value)
            new_list.append(current_1.next.value)
            break
        new_list.append(current_2.value)
        new_list.append(current_1.next.value)
        current_1 = current_1.next
        current_2 = current_2.next

    return new_list


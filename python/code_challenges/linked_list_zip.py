from data_structures.linked_list import LinkedList

def zip_lists(a, b):
    newList = LinkedList()
    current1 = a.head
    current2 = b.head
    if a.head == None:
        return b
    if b.head == None:
        return a
    newList.insert(current1.value)

    while newList:
        print(current1.next, current2.next)
        if current1.next == None and current2.next == None:
            newList.append(current2.value)
            break
        if current1.next == None and current2.next != None:
            newList.append(current2.value)
            next_value = current2.next
            newList.append(next_value.value)
            break
        if current1.next != None and current2.next == None:
            newList.append(current2.value)
            newList.append(current1.next.value)
            break
        newList.append(current2.value)
        newList.append(current1.next.value)
        current1 = current1.next
        current2 = current2.next
    print(newList)

    return newList


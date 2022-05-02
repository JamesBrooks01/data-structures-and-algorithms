from data_structures.linked_list import LinkedList

new_list = LinkedList()
new_list.insert("t")
new_list.insert("a")
new_list.insert("c")
new_list.insert("o")
new_list.insert("c")
new_list.insert("a")
new_list.insert("t")

def palindrome_check(link_list):
  original_list = str(link_list)
  print("OG", original_list)

  previous = None
  current = link_list.head
  next = current.next
  # print(previous)
  # print(current.value)
  # print(next.value)

  while next is not None:
    current.next = previous
    print("current.next", current.next)
    previous = current
    print("previous", previous.value)
    current = next
    print("current", current.value)
    next = current.next
    print("next", next)

  reversed_list = str(link_list)
  print("RL", reversed_list)


palindrome_check(new_list)

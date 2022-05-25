def merge_sort(lst):
  n = len(lst)
  if n > 1:
    mid = n//2
    left = lst[0:mid]
    right = lst[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,lst)
  return lst

def merge(left,right,lst):
  i = j = k = 0

  while i < len(left) and j < len(right):

    if left[i] <= right[j]:
      lst[k] = left[i]
      i += 1
    else:
      lst[k] = right[j]
      j += 1

    k +=1

  if i == len(left):
    for x in range(j, len(right)):
      lst[k] = right[x]
      k += 1
  else:
    for x in range(i, len(left)):
      lst[k] = left[x]
      k += 1
  return lst

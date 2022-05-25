# Merge Sort

## Pseudocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace

Sample Array: `[8,4,23,42,16,15]`

Pass 1:

![merge_sort_pass_1](./images/Merge%20Sort.png)

In the first pass through, the left and right are [4] and [23] and loops through once then merges the two and returns [4,23]

Pass 2:

![merge_sort_pass_2](./images/Merge%20Sort%20(1).png)

In the second pass through, the left is [8] and the right is [4,23]. It loops through twice and then merges them and returns [4,8,23]

Pass 3:

![merge_sort_pass_3](./images/Merge%20Sort%20(2).png)

In the third pass through, the left is [16] and the right is [15]. It looks through once and then merges and returns [15,16]

Pass 4:

![merge_sort_pass_4](./images/Merge%20Sort%20(3).png)

In the fourth pass through, the left is [42] and the right is [15,16]. It loops through twice and then merges and returns [15,16,42]

Pass 5:

![merge_sort_pass_5](./images/Merge%20Sort%20(4).png)

On the last play through, the left is [4,8,23] and the right is [15,16,42]. It loops through 5 times and then merges and returns [4,8,15,16,23,42]

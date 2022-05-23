# Insertion Sort

## Pseudocode

```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## Trace

Sample Array: `[8,4,23,42,16,15]`

Pass 1:

![insertion_sort_pass_1](./images/Insertion%20Sort.png)

In the first pass through of the insertion sort, we check if there is a greater number previously in the array than the current number. We find it immediately and insert the current number at the next space and then set the current space to the greater value. The result is the two numbers get swapped with the smaller number at the beginning.

Pass 2:

![insertion_sort_pass_2](./images/Insertion%20Sort%20(1).png)

In the second pass, as before we check if there is a greater number previously in the array than the current number. It is not found and thus the current number sets itself to temp.

Pass 3:

![insertion_sort_pass_3](./images/Insertion%20Sort%20(2).png)

In the third pass, the same thing as in pass 2 happens with no greater number being found previously in the array and it replaces itself with temp.

Pass 4:

![insertion_sort_pass_4](./images/Insertion%20Sort%20(3).png)

In the fourth pass, it goes through the while loop twice finding a greater value than the current value twice and following the process of swapping the values through insertion for each until it reached a value that was less than the current.

Pass 5:

![insertion_sort_pass_5](./images/Insertion%20Sort%20(4).png)

In the fifth pass, it goes through the while loop thrice before finding a value that is smaller than the current value and along the way follows the pattern of swapping the values.

After this pass, it would increment i to 6 and break the for loop, leaving the array sorted.


## Efficiency

- Time O(n^2)
  - The main operation of the algorithm is comparison and runs n*(n-1) times leaving it at n squared time complexity.
- Space O(1)
  - No additional space is created and sorts the array in place leaving the space complexity at O(1)

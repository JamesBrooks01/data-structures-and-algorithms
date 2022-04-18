# Reverse an Array

Our task is to whiteboard out the task of reversing an array by defining the input and output of the function, what test cases to work with and a visualization of how the algorithm or function works.

## Whiteboard Process

![array_reverse Image](./Code%20Challenge%2001%20Whiteboard.png)

## Approach & Efficiency

I took the approach of mutating the array by creating an algorithm that keeps track of the previous current and next values and in a visual manner, reverses the order of the elements. I chose to do it this way because it engages my brain to this method of whiteboarding better as it is a slower and more complicated to explain method than my prefered method of looping through the array backwards and assigning each value to a new array. I believe that the Big O for this approach is O(N) because the longer the array it has to work through, the more times it will have to loop through the array to reach the end and thus it grows linearly with the size of the data set.

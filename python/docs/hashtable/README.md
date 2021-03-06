# Hashtables

Our task was to create a class called Hashtable that behaves according to the name with the following methods(further described in the API section);

- `hash()`
- `set()`
- `get()`
- `contains()`
- `keys()`

- The way I coded the contains method was inspired by a student who shared their code in class on 05-31-22

## Approach & Efficiency

I took the approach of treating each 'bucket' as a linked list.
For each method, the Big O would be;

- Hash
  - O(n) for time as it has a for loop that goes through the input key.
  - O(1) for space as it makes simple calculations then returns a number
- Set
  - O(1) for time as each step has a single place it goes to and can go there in one step.
  - O(1) for space as it doesn't store anything within the function and only adds a single key/value to the Hashtable at a time through the Linked List insert method which is O(1).
- Get
  - O(n) for time as it loops through the linked list at the desired 'bucket' to deal with any collisions.
  - O(1) for space at it doesn't store anything within the function that grows in size.
- Contains
  - O(n) for time because it uses the Get method to check for a value.
  - O(1) for space as it doesn't store anything that grows in size
- Keys
  - O(1) for both time and space as it just returns a list that is built and created as the Hashtable is used.

## API

- Hash
  - The hash method takes in a key in the form of a string that using a for loop, turns each character into it's unicode value and sums up the whole thing, then multiplies it by a prime number and then divides it by the size of the Hashtable. Finally returning the resulting number.
- Set
  - The set method takes in a key and a value, then calls the hash method for the key and sets a variable to the self.buckets[index] variable. Then if the targeted bucket is empty, creates an empty Linked List and sets the targeted bucket to it. Then it uses the Insert method from the Linked List to add the parameter value to it. Finally, to assist with another method, if the parameter key doesn't exist in the relevent list, appends the key to the list.
- Get
  - The get method takes in a key and then through a while loop, searches the index location of the key for the correct value, returning the appropriate value, None otherwise.
- Contains
  - The contains method calls the get method and converts the result into a boolean value that it then returns.
- Keys
  - The keys method simply returns the list of keys generated by the set method.

[Link to Code](../../data_structures/hashtable.py)

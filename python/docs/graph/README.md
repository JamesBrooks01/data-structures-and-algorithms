# Graphs

## Challenge

Our task is to code out our own implementation of a Graph. It should be represented as an Adjacency List and have the following methods which are described further in the API section;

- `add_node()`
- `add_edge()`
- `get_nodes()`
- `get_neighbors()`
- `size()`

## Approach & Efficiency

- `add_node()`
  - Time: O(1) because both of the steps would be identical irrelevant of the input.
  - Space: O(n) because the size of the vertex would increase with the size of the input.
- `add_edge()`
  - Time: O(1) because all of the steps operate the same irrelevant of the inputs.
  - Space: O(1) because the operation would take up the same space for the inputs.
- `get_nodes()`
  - Time: O(1) because it is just returning the result of the keys method on the dictionary.
  - Space: O(1) because it is only returning the keys of the adjacency list.
- `get_neighbors()`
  - Time: O(1) because it is grabbing a from a specified key in a dictionary.
  - Space: O(1) because it is directly returning a value from a dictionary.
- `size()`
  - Time: O(1) because it is using the len function on the dictionary, which is an O(1) operation.
  - Space: O(1) because it is directly returning the result of the len function.

## API

- `add_node()`
  - The add_node method takes in a value and returns the vertex created. It first creates a new instance of the Vertex class and then adds a new dictionary key of the new vertex with a value of an empty list. Finally, returning the new vertex.
- `add_edge()`
  - The add_edge method takes in a start_vertex, and end_index, and an optional weight parameter and returns nothing. It first verifies that both the start and end vertices are in the adjacency list, returning a KeyError if one is not. Then it creates a new instance of the Edge class and then adds the edge instance to the appropriate vertex in the adjacency list.
- `get_nodes()`
  - The get_nodes method calls the keys method on the adjacency list and returns the result.
- `get_neighbors()`
  - The get_neighbors method takes in a vertex and accesses the value in the adjacency list with that key and returns it.
- `size()`
  - The size method calls the len function on the adjacency list and returns the result.

[Link to Code](../../data_structures/graph.py)

# Challenge Summary 37

Our task was to write out a function that takes in a graph and a list of names and determine if the path presented is possible and if so, return True and the cost of the trip.

## Whiteboard Process

![graph_business_trip.png](./graph_business_trip.png)

## Approach & Efficiency

I took the approach of building dictionaries for the vertices and the neighbors for each to be used later in the code. The main part of the code iterates through the list of city names and for each city vertex check the list of neighbors for the next city name in the list and if so, increment a variable for the total cost breaking the loop once found. Then finally at the end, if the total cost is above 0, it returns a tuple of True and the total cost.
However, due to this approach the Big O for this isn't very good which to me means that there has to be a way solve this issue better which when I have time, plan to try and find.

- Time: O(n^2)
  - This is because I have a nested for loop that iterates through the city list and then the list of neighbors for the current city
- Space: O(n)
  - This is because I do fill up two dictionaries with all the vertices in the graph for one, and the second with all the neighbors for each.
  - I could potentially try trimming this down a bit by attempting to grab only the neighbors of the cities that exist in the city name list, but the space would still be O(n). Still, it is a potential way to increase the efficiency of the code.

[Link to Code](../../code_challenges/graph_business_trip.py)
